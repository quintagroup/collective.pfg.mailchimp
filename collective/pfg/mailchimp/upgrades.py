from logging import getLogger

default_profile = 'profile-collective.pfg.mailchimp:default'
logger = getLogger('collective.pfg.mailchimp:upgrade')


def upgrade_to_1_0_1(context):
    logger.info("Upgrading to 1.0.1")
    context.runImportStepFromProfile(default_profile, 'typeinfo')
