import Vue from 'vue'
import Vuex from 'vuex'
import user from './userInfo'
import usertweets from './userTweets'
import total from './tweetsTotal'
import sentiments from './sentiments'
import mutations from './mutations'
import usercomment from './userComment'
import tempid from './tempId'
import tempids from './tempids'
import group from './group'

Vue.use(Vuex)

export default new Vuex.Store({
  user,
  usertweets,
  tempid,
  tempids,
  group,
  usercomment,
  total,
  sentiments,
  mutations
})
