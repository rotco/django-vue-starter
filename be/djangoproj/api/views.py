from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseServerError
from django.views import View
import requests
import json
import pandas as pd
from datetime import datetime

DATE_FORMAT = "%b/%d/%Y"


def get_df_from_csv(url):
    try:
        df = pd.read_csv(url)
        return df
    except FileNotFoundError:
        msg = "File not found"
        print(msg)
        return JsonResponse({"error": msg}, status=404)
    except pd.errors.EmptyDataError:
        msg = "CSV file is empty"
        print(msg)
        return JsonResponse({"error": msg}, status=500)
    except pd.errors.ParserError:
        msg = "CSV parsing error"
        print(msg)
        return JsonResponse({"error": msg}, status=500)


def convert_extended_candidate_to_dict(df):
    extended_dict = {}
    try:
        for _, row in df.iterrows():
            phone = str(row["Phone Number"])
            linkedin = row["Linkedin"]
            if phone:
                extended_dict[phone] = {"linkedin": linkedin}
        return extended_dict
    except KeyError:
        msg = "KeyError while trying to access candidate keys"
        print(msg)
        return JsonResponse({"error": msg}, status=500)


def normalize_experience(experience):
    sorted_experiences = sorted(
        experience,
        key=lambda x: datetime.strptime(x["start_date"], DATE_FORMAT),
    )
    results = []
    last_end = None
    for exp in sorted_experiences:
        text = f"Worked as: Programmer, From {exp['start_date']} To {exp.get('end_date', 'Now')}"

        if last_end:
            start = datetime.strptime(exp["start_date"], DATE_FORMAT)
            date_difference = start - last_end

            gap = date_difference.days
            if gap > 0:
                results.append(f"Gap between jobs: {gap} days")
        else:
            end = exp.get("end_date", datetime.now())
            last_end = datetime.strptime(end, DATE_FORMAT)
        results.append(text)
    return results


def normalize_candidates(candidates, extended_cand_dict):
    results = []
    for cand in candidates:
        phone_raw = cand.get("contact_info", {}).get("phone")
        if phone_raw:
            phone = phone_raw.replace("-", "")
            linkedin_cand = None
            if phone in extended_cand_dict:
                linkedin_cand = extended_cand_dict.get(phone, {}).get("linkedin")
        normalized_experience = normalize_experience(cand["experience"])
        results.append(
            {
                "name": cand["contact_info"]["name"]["formatted_name"],
                "linkedin": linkedin_cand,
                "experience": normalized_experience,
            }
        )
    return results


class ResumeList(View):
    def get(self, request, resume_path):
        base_url = "https://hs-recruiting-test-resume-data.s3.amazonaws.com/"
        print(resume_path)
        url = base_url + resume_path
        try:
            response = requests.get(url)
            if response.ok:
                candidates = response.json()
                df = get_df_from_csv(
                    "https://hs-recruiting-test-resume-data.s3.amazonaws.com/linkedin_source_b1f6-acde48001122.csv"
                )
                extended_cand_dict = convert_extended_candidate_to_dict(df)

                normalized_candidates = normalize_candidates(
                    candidates, extended_cand_dict
                )
                print(normalized_candidates)
                return JsonResponse({"results": normalized_candidates})
            else:
                raise response.raise_for_status()
        except requests.RequestException as e:
            print("error: ", e)
            return JsonResponse({"error": e}, status=response.status_code)
        except TypeError as e:
            print("could not read the content.", e)
            return JsonResponse({"error": "could not read the content"}, status=500)
