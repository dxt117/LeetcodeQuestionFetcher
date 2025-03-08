# -*- coding: utf-8 -*-
# 力扣中文官网题库页面 https://leetcode.cn/problemset/

# 力扣中文官网题目请求的api
URL = "https://leetcode.cn/graphql/"

# 原始查询语句：查询题目描述
QUERY_DESCRIPTION = '''
    query questionDetail($titleSlug: String!) {
  languageList {
    id
    name
    verboseName
  }
  statusList {
    id
    name: translatedName
  }
  question(titleSlug: $titleSlug) {
    title
    titleSlug
    questionId
    questionFrontendId
    questionTitle
    translatedTitle
    content
    translatedContent
    categoryTitle
    difficulty
    stats
    style
    contributors {
      username
      profileUrl
      avatarUrl
    }
    book {
      id
      bookName
      pressName
      source
      shortDescription
      fullDescription
      bookImgUrl
      pressImgUrl
      productUrl
    }
    companyTagStatsV2
    topicTags {
      name
      slug
      translatedName
    }
    similarQuestions
    mysqlSchemas
    dataSchemas
    frontendPreviews
    likes
    dislikes
    isPaidOnly
    status
    boundTopicId
    enableTestMode
    metaData
    enableRunCode
    enableSubmit
    envInfo
    isLiked
    nextChallengePairs
    libraryUrl
    hints
    codeSnippets {
      code
      lang
      langSlug
    }
    jsonExampleTestcases
    exampleTestcases
    sampleTestCase
    hasFrontendPreview
    editorType
  }
}
'''

# 原始查询语句：查询题目标题
QUERY_TITLE_SLUG = '''
    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList(
    categorySlug: $categorySlug
    limit: $limit
    skip: $skip
    filters: $filters
  ) {
    hasMore
    total
    questions {
      acRate
      difficulty
      freqBar
      frontendQuestionId
      isFavor
      paidOnly
      solutionNum
      status
      title
      titleCn
      titleSlug
      topicTags {
        name
        nameTranslated
        id
        slug
      }
      extra {
        hasVideoSolution
        topCompanyTags {
          imgUrl
          slug
          numSubscribed
        }
      }
    }
  }
}
'''
