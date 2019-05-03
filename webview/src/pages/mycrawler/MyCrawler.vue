<template>
  <div>
    <common-header></common-header>
    <my-scrapyd></my-scrapyd>
    <common-footer></common-footer>
    <bg-color></bg-color>
  </div>
</template>

<script>
import CommonHeader from 'common/Header'
import CommonFooter from 'common/Footer'
import BgColor from 'common/BgSet'
import MyScrapyd from './components/Demo'

export default {
  name: 'MyCrawler',
  components: {
    CommonHeader,
    MyScrapyd,
    CommonFooter,
    BgColor
  }
}

</script>

<style lang="scss" scoped>

</style>
