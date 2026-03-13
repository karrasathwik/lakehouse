{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "4f08079d-a673-453d-b845-997a98e6344e",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "pipeline {\n",
    "    agent any\n",
    "\n",
    "    stages {\n",
    "        stage('Checkout Code') {\n",
    "            steps {\n",
    "                git branch: 'main', url: 'https://github.com/karrasathwik/lakehouse.git'\n",
    "            }\n",
    "        }\n",
    "\n",
    "        stage('Deploy Extract Notebook') {\n",
    "            steps {\n",
    "                sh '''\n",
    "                databricks workspace import \"extract 2026-03-03 16_08_56.ipynb\" /Repos/lakehouse/extract.ipynb -o\n",
    "                '''\n",
    "            }\n",
    "        }\n",
    "\n",
    "        stage('Deploy Silver Notebook') {\n",
    "            steps {\n",
    "                sh '''\n",
    "                databricks workspace import \"silver 2026-03-05 12_30_40.ipynb\" /Repos/lakehouse/silver.ipynb -o\n",
    "                '''\n",
    "            }\n",
    "        }\n",
    "\n",
    "        stage('Deploy Gold Notebook') {\n",
    "            steps {\n",
    "                sh '''\n",
    "                databricks workspace import \"gold 2026-03-10 08_07_34.ipynb\" /Repos/lakehouse/gold.ipynb -o\n",
    "                '''\n",
    "            }\n",
    "        }\n",
    "    }\n",
    "\n",
    "    post {\n",
    "        success {\n",
    "            echo 'Notebooks deployed successfully!'\n",
    "        }\n",
    "        failure {\n",
    "            echo 'Deployment failed!'\n",
    "        }\n",
    "    }\n",
    "}"
   ]
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "computePreferences": null,
   "dashboards": [],
   "environmentMetadata": {
    "base_environment": "",
    "environment_version": "4"
   },
   "inputWidgetPreferences": null,
   "language": "python",
   "notebookMetadata": {
    "pythonIndentUnit": 4
   },
   "notebookName": "jenkins.yml",
   "widgets": {}
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
