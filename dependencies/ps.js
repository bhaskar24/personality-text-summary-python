var PersonalityTextSummaries = require('./personality-text-summary.standalone.js');
// locale is one of {'en', 'es', 'ja', 'ko'}.  version refers to which version of Watson Personality Insights to use, v2 or v3.
var v3EnglishTextSummaries = new PersonalityTextSummaries({ locale: 'es', version: 'v2' });
// reads in json
var myV3EnPersonalityProfile = require('./result.json');
// retrieve the summary for a specified personality profile (json)
var textSummary  = v3EnglishTextSummaries.getSummary(myV3EnPersonalityProfile);
console.log(textSummary);
