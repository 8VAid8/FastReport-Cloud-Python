# coding: utf-8

# flake8: noqa
"""
    FastReport Cloud

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from fastreport_cloud_sdk.models.admin_export_folder_create_vm import AdminExportFolderCreateVM
from fastreport_cloud_sdk.models.admin_permission import AdminPermission
from fastreport_cloud_sdk.models.admin_report_folder_create_vm import AdminReportFolderCreateVM
from fastreport_cloud_sdk.models.admin_subscription_vm import AdminSubscriptionVM
from fastreport_cloud_sdk.models.admin_subscriptions_vm import AdminSubscriptionsVM
from fastreport_cloud_sdk.models.admin_template_folder_create_vm import AdminTemplateFolderCreateVM
from fastreport_cloud_sdk.models.analysis_result_vm import AnalysisResultVM
from fastreport_cloud_sdk.models.analysis_results_vm import AnalysisResultsVM
from fastreport_cloud_sdk.models.api_key_vm import ApiKeyVM
from fastreport_cloud_sdk.models.api_keys_vm import ApiKeysVM
from fastreport_cloud_sdk.models.breadcrumbs_model import BreadcrumbsModel
from fastreport_cloud_sdk.models.breadcrumbs_vm import BreadcrumbsVM
from fastreport_cloud_sdk.models.count_vm import CountVM
from fastreport_cloud_sdk.models.create_api_key_vm import CreateApiKeyVM
from fastreport_cloud_sdk.models.create_data_source_admin_vm import CreateDataSourceAdminVM
from fastreport_cloud_sdk.models.create_data_source_vm import CreateDataSourceVM
from fastreport_cloud_sdk.models.create_group_admin_vm import CreateGroupAdminVM
from fastreport_cloud_sdk.models.create_group_vm import CreateGroupVM
from fastreport_cloud_sdk.models.create_subscription_invite_vm import CreateSubscriptionInviteVM
from fastreport_cloud_sdk.models.create_subscription_period_vm import CreateSubscriptionPeriodVM
from fastreport_cloud_sdk.models.create_subscription_plan_vm import CreateSubscriptionPlanVM
from fastreport_cloud_sdk.models.create_subscription_vm import CreateSubscriptionVM
from fastreport_cloud_sdk.models.data_source_permission import DataSourcePermission
from fastreport_cloud_sdk.models.data_source_permissions import DataSourcePermissions
from fastreport_cloud_sdk.models.data_source_permissions_vm import DataSourcePermissionsVM
from fastreport_cloud_sdk.models.data_source_vm import DataSourceVM
from fastreport_cloud_sdk.models.data_sources_vm import DataSourcesVM
from fastreport_cloud_sdk.models.default_permissions import DefaultPermissions
from fastreport_cloud_sdk.models.default_permissions_vm import DefaultPermissionsVM
from fastreport_cloud_sdk.models.delete_api_key_vm import DeleteApiKeyVM
from fastreport_cloud_sdk.models.export_create_admin_vm import ExportCreateAdminVM
from fastreport_cloud_sdk.models.export_folder_create_vm import ExportFolderCreateVM
from fastreport_cloud_sdk.models.export_report_task_vm import ExportReportTaskVM
from fastreport_cloud_sdk.models.export_template_task_vm import ExportTemplateTaskVM
from fastreport_cloud_sdk.models.export_vm import ExportVM
from fastreport_cloud_sdk.models.exports_vm import ExportsVM
from fastreport_cloud_sdk.models.file_icon_vm import FileIconVM
from fastreport_cloud_sdk.models.file_permission import FilePermission
from fastreport_cloud_sdk.models.file_permissions import FilePermissions
from fastreport_cloud_sdk.models.file_permissions_vm import FilePermissionsVM
from fastreport_cloud_sdk.models.file_rename_vm import FileRenameVM
from fastreport_cloud_sdk.models.file_tags_update_vm import FileTagsUpdateVM
from fastreport_cloud_sdk.models.file_update_vm import FileUpdateVM
from fastreport_cloud_sdk.models.file_vm import FileVM
from fastreport_cloud_sdk.models.files_vm import FilesVM
from fastreport_cloud_sdk.models.folder_icon_vm import FolderIconVM
from fastreport_cloud_sdk.models.folder_rename_vm import FolderRenameVM
from fastreport_cloud_sdk.models.folder_tags_update_vm import FolderTagsUpdateVM
from fastreport_cloud_sdk.models.group_permission import GroupPermission
from fastreport_cloud_sdk.models.group_permissions import GroupPermissions
from fastreport_cloud_sdk.models.group_permissions_vm import GroupPermissionsVM
from fastreport_cloud_sdk.models.group_user_vm import GroupUserVM
from fastreport_cloud_sdk.models.group_users_vm import GroupUsersVM
from fastreport_cloud_sdk.models.group_vm import GroupVM
from fastreport_cloud_sdk.models.groups_vm import GroupsVM
from fastreport_cloud_sdk.models.invited_user import InvitedUser
from fastreport_cloud_sdk.models.prepare_template_task_vm import PrepareTemplateTaskVM
from fastreport_cloud_sdk.models.problem_details import ProblemDetails
from fastreport_cloud_sdk.models.register_user_vm import RegisterUserVM
from fastreport_cloud_sdk.models.rename_data_source_vm import RenameDataSourceVM
from fastreport_cloud_sdk.models.rename_group_vm import RenameGroupVM
from fastreport_cloud_sdk.models.rename_subscription_vm import RenameSubscriptionVM
from fastreport_cloud_sdk.models.report_create_admin_vm import ReportCreateAdminVM
from fastreport_cloud_sdk.models.report_create_vm import ReportCreateVM
from fastreport_cloud_sdk.models.report_folder_create_vm import ReportFolderCreateVM
from fastreport_cloud_sdk.models.report_info import ReportInfo
from fastreport_cloud_sdk.models.report_vm import ReportVM
from fastreport_cloud_sdk.models.reports_vm import ReportsVM
from fastreport_cloud_sdk.models.subscription_folder import SubscriptionFolder
from fastreport_cloud_sdk.models.subscription_invite_vm import SubscriptionInviteVM
from fastreport_cloud_sdk.models.subscription_invites_vm import SubscriptionInvitesVM
from fastreport_cloud_sdk.models.subscription_period_vm import SubscriptionPeriodVM
from fastreport_cloud_sdk.models.subscription_permission import SubscriptionPermission
from fastreport_cloud_sdk.models.subscription_permissions import SubscriptionPermissions
from fastreport_cloud_sdk.models.subscription_permissions_vm import SubscriptionPermissionsVM
from fastreport_cloud_sdk.models.subscription_plan_vm import SubscriptionPlanVM
from fastreport_cloud_sdk.models.subscription_plans_vm import SubscriptionPlansVM
from fastreport_cloud_sdk.models.subscription_user_vm import SubscriptionUserVM
from fastreport_cloud_sdk.models.subscription_users_vm import SubscriptionUsersVM
from fastreport_cloud_sdk.models.subscription_vm import SubscriptionVM
from fastreport_cloud_sdk.models.subscriptions_vm import SubscriptionsVM
from fastreport_cloud_sdk.models.template_create_admin_vm import TemplateCreateAdminVM
from fastreport_cloud_sdk.models.template_create_vm import TemplateCreateVM
from fastreport_cloud_sdk.models.template_folder_create_vm import TemplateFolderCreateVM
from fastreport_cloud_sdk.models.template_vm import TemplateVM
from fastreport_cloud_sdk.models.templates_vm import TemplatesVM
from fastreport_cloud_sdk.models.update_data_source_connection_string_vm import UpdateDataSourceConnectionStringVM
from fastreport_cloud_sdk.models.update_data_source_permissions_vm import UpdateDataSourcePermissionsVM
from fastreport_cloud_sdk.models.update_data_source_subscription_vm import UpdateDataSourceSubscriptionVM
from fastreport_cloud_sdk.models.update_data_source_vm import UpdateDataSourceVM
from fastreport_cloud_sdk.models.update_default_permissions_vm import UpdateDefaultPermissionsVM
from fastreport_cloud_sdk.models.update_file_permissions_vm import UpdateFilePermissionsVM
from fastreport_cloud_sdk.models.update_group_permissions_vm import UpdateGroupPermissionsVM
from fastreport_cloud_sdk.models.update_group_vm import UpdateGroupVM
from fastreport_cloud_sdk.models.update_subscription_locale_vm import UpdateSubscriptionLocaleVM
from fastreport_cloud_sdk.models.update_subscription_permissions_vm import UpdateSubscriptionPermissionsVM
from fastreport_cloud_sdk.models.update_subscription_plan_vm import UpdateSubscriptionPlanVM
from fastreport_cloud_sdk.models.update_subscription_vm import UpdateSubscriptionVM
from fastreport_cloud_sdk.models.update_user_vm import UpdateUserVM
from fastreport_cloud_sdk.models.user_profile_update_vm import UserProfileUpdateVM
from fastreport_cloud_sdk.models.user_profile_vm import UserProfileVM
from fastreport_cloud_sdk.models.user_vm import UserVM
from fastreport_cloud_sdk.models.users_vm import UsersVM
