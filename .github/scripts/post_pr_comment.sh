generate_post_data()
{
  cat <<EOF
{
  "body": "$(cat gh-pr-comment.log | sed -z 's/\n/\\n/g')"
}
EOF
}
PR_NUMBER=$(jq --raw-output .pull_request.number "$GITHUB_EVENT_PATH")
curl -s -H "Authorization: token ${KEY4HEP_COMMENT_BOT_TOKEN}" \
 -X POST -d "$(generate_post_data)"  \
 "https://api.github.com/repos/${GITHUB_REPOSITORY}/issues/${PR_NUMBER}/comments"

