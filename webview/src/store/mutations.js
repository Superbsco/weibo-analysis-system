export default {
  changeUserTweets (state, usertweets) {
    state.usertweets = usertweets
    // try {
    //   localStorage.tweets = usertweets
    // } catch (e) {}
  },
  changeSentiments (state, sentiments) {
    state.sentiments = sentiments
  }
}
