<template>
  <div>
    <common-header></common-header>
    <group-main></group-main>
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
import GroupMain from './components/GroupMain'

export default {
  name: 'UserComment',
  components: {
    CommonHeader,
    GroupMain,
    ScrollTop,
    CommonFooter,
    BgColor
  }
}

</script>

<style lang="scss" scoped>

</style>
