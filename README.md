# Glue-job-skeleton

This repository has a base skeleton structure for AWS glue jobs

### 1. Prerequisite

- python 3.6
- spark 2.4.3
- AWS-glue-libs 
  - https://github.com/awslabs/aws-glue-libs
  - add the path of lib to PYTHONPATH and PATH
  
### 2. Setup and Run application from local

1. Fetch code from GitLab (Repository)
    ```
    git clone https://github.com/abhijeet0051997/script-skeleton.git
    ```
2. Navigate to project directory.
    ```
    cd script-skeleton
    ```
3. Install dependencies
    ```
   make deps_dev
    ```
4. Build project
    ```
    make build 
    ```
5. Submit spark job
    ```
    make local_submit 
    ```