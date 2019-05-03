<template>
  <div>
    <common-header></common-header>
    <index-main></index-main>
    <common-footer></common-footer>
    <bg-color></bg-color>
  </div>
</template>

<script>
import BgColor from 'common/BgSet'
import CommonHeader from 'common/Header'
import CommonFooter from 'common/Footer1'
import IndexMain from './components/Main'

export default {
  name: 'Index',
  components: {
    BgColor,
    CommonHeader,
    IndexMain,
    CommonFooter
  },
  data () {
    return {}
  },
  computed: {},
  methods: {},
  mounted () {},
  activated () {}
}

</script>

<style lang="scss">
</style>
