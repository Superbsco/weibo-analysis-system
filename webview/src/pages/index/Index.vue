<template>
  <div>
      <index-header></index-header>
      <index-logo></index-logo>
      <index-footer></index-footer>
      <bg-color></bg-color>
  </div>
</template>

<script>
import BgColor from 'common/BgSet'
import CommonHeader from 'common/Header'
import CommonFooter from 'common/Footer'
import IndexLogo from './components/Logo'

export default {
  name: 'Index',
  components: {
    BgColor,
    IndexHeader,
    IndexLogo,
    IndexFooter
  },
  data () {
    return {
    }
  },
  computed: {
  },
  methods: {
  },
  mounted () {
  },
  activated () {
  }
}
</script>

<style lang="scss">
</style>
