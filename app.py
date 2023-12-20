import streamlit as st
import requests
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()
bitrise_token = os.getenv('BITRISE_API_TOKEN')
bitrise_workflow = os.getenv('BITRISE_WORKFLOW')
bitrise_app_slug = os.getenv('BITRISE_APP_SLUG')

# Streamlit 页面布局
st.title('Bitrise Build Trigger')
branch_name = st.text_input('Enter the branch name:')
trigger_button = st.button('Trigger Build')


def trigger_build(branch_name, workflow, app_slug):
    url = f'https://api.bitrise.io/v0.1/apps/{app_slug}/builds'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'token {bitrise_token}'
    }
    payload = {
        "hook_info": {
            "type": "bitrise"
        },
        "build_params": {
            "branch": branch_name,
            "workflow_id": workflow
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()


if trigger_button and branch_name:
    result = trigger_build(branch_name, bitrise_workflow, bitrise_app_slug)
    st.write(result)
