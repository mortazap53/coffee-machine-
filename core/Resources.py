def tracking_resources(water, coffee, milk):
    resources["water"] = resources["water"] - water
    resources["coffee"] = resources["coffee"] - coffee
    resources["milk"] = resources["milk"] - milk
    return resources

resources = {
    "water": 500,
    "coffee": 500,
    "milk": 300,
}