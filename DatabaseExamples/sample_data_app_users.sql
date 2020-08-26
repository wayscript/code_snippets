CREATE TABLE marketing_emails(
   id serial PRIMARY KEY,
   email_string VARCHAR (50) NOT NULL,
   email_domain VARCHAR (150) NOT NULL,
   age INT,
   gender VARCHAR(50),
   location VARCHAR(150),
   job_role VARCHAR(150),
   accounting_usage FLOAT(4,2),
   creative_usage FLOAT(4,2),
   crm_usage FLOAT(4,2),
   devops_usage FLOAT(4,2),
   diagramming_usage FLOAT(4,2),
   email_usage FLOAT(4,2),
   email_marketing_usage FLOAT(4,2),
   erp_usage FLOAT(4,2),
   file_management_usage FLOAT(4,2),
   human_resources_usage FLOAT(4,2),
   org_communication_usage FLOAT(4,2),
   project_management_usage FLOAT(4,2),
   social_media_usage FLOAT(4,2),
);

INSERT INTO marketing_emails (email_string, email_domain, age, gender, location, job_role, accounting_usage, creative_usage, crm_usage, devops_usage, diagramming_usage, email_usage, email_marketing_usage, erp_usage, file_management_usage, human_resources_usage, org_communication_usage, project_management_usage, social_media_usage) VALUES ('TimHP', 'HP.com', 49, 'male', 'Denver, Colorado', 'developer', 00.00, 00.05, 00.00, 00.05, 00.00, 00.00, 00.00, 00.05, 00.55, 00.00, 00.00, 00.20, 00.00)


