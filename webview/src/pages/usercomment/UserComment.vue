<template>
  <div>
    <common-header></common-header>
    <comment-header></comment-header>
    <scroll-top></scroll-top>
    <bg-color></bg-color>
    <common-footer></common-footer>
  </div>
</template>

<script>
import CommonHeader from 'common/Header'
import ScrollTop from 'common/ScrollToTop'
import CommonFooter from 'common/Footer'
import BgColor from 'common/BgSet'
import CommentHeader from './components/CommentHeader'

export default {
  name: 'UserComment',
  components: {
    CommonHeader,
    CommentHeader,
    ScrollTop,
    CommonFooter,
    BgColor
  }
}

</script>

<style lang="scss" scoped>

</style>
