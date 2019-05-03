<template>
  <div>
    <common-header></common-header>
    <comment-main></comment-main>
    <common-footer></common-footer>
    <bg-color></bg-color>
  </div>
</template>

<script>
import CommonHeader from 'common/Header'
import CommonFooter from 'common/Footer1'
import BgColor from 'common/BgSet'
import CommentMain from './components/CommentMain'

export default {
  name: 'Comment',
  components: {
    CommonHeader,
    CommentMain,
    CommonFooter,
    BgColor
  }
}

</script>

<style lang="scss" scoped>

</style>
