generate_new_version_data()
{
  cat <<EOF
{
  "body": "$(cat gh-new-version.log | sed -z 's/\n/\\n/g')\n"
}
EOF
}
cat gh-new-version.log
echo $(generate_new_version_data)
if [[ -f gh-new-version.log ]]; then
  curl -s -H "Authorization: token ${KEY4HEP_COMMENT_BOT_TOKEN}" \
   -X POST -d "$(generate_new_version_data)"  \
   "https://api.github.com/repos/${GITHUB_REPOSITORY}/issues/238/comments"
else
  echo "No new versions found"
fi

