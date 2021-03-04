grep "^ -" key4hep-stack-concretization.log > key4hep-stack-concretization-newpackages.log
echo "## New packages at next release after merge:" > gh-pr-comment.log
echo " " >> gh-pr-comment.log
echo "\`\`\`" >> gh-pr-comment.log
cat key4hep-stack-concretization-newpackages.log >> gh-pr-comment.log
echo "\`\`\`" >> gh-pr-comment.log
echo " " >> gh-pr-comment.log
echo "## Full List of Packages: " >> gh-pr-comment.log
echo " " >> gh-pr-comment.log
echo "<details>" >> gh-pr-comment.log
echo " " >> gh-pr-comment.log
echo "\`\`\`" >> gh-pr-comment.log
cat key4hep-stack-concretization.log >> gh-pr-comment.log
echo "\`\`\`" >> gh-pr-comment.log
echo " " >> gh-pr-comment.log
echo "</details>" >> gh-pr-comment.log
