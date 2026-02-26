 git init
 git add .


 (my_project_env) PS C:\Users\hongf\miniconda3\envs\minimind-master> git branch
(my_project_env) PS C:\Users\hongf\miniconda3\envs\minimind-master> git remote add origin https://github.com/Qihongfei-hub/my_minimind.git
(my_project_env) PS C:\Users\hongf\miniconda3\envs\minimind-master> git remote -v
origin  https://github.com/Qihongfei-hub/my_minimind.git (fetch)
origin  https://github.com/Qihongfei-hub/my_minimind.git (push)
(my_project_env) PS C:\Users\hongf\miniconda3\envs\minimind-master> git branch                            
(my_project_env) PS C:\Users\hongf\miniconda3\envs\minimind-master> git commit -m "Initial commit"


 PS C:\Users\hongf\miniconda3\envs\minimind-master> git status
On branch master
nothing to commit, working tree clean
(my_project_env) PS C:\Users\hongf\miniconda3\envs\minimind-master> git branch -m master main
(my_project_env) PS C:\Users\hongf\miniconda3\envs\minimind-master> git push -u origin main


为了避免后续推送时需要指定分支，可以设置默认推送分支：
git push --set-upstream origin master


在团队协作中，记得定期拉取远程更新：
git pull origin main

分支管理 ：如果需要开发新功能，建议创建新分支
git checkout -b feature-branch

提交规范 ：遵循良好的提交信息规范，有助于代码维护
git commit -m "feat: 添加新功能"  # 功能开发
git commit -m "fix: 修复bug"      # 错误修复
git commit -m "docs: 更新文档"     # 文档更新
