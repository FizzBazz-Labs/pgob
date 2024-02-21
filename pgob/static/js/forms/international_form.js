const { createApp, ref } = Vue

createApp({
  data() {
    return {
      showMediaChannels: false,
      headOfDelegations: [1,2,3,4,5,6],
      suppliers: [7,8],
      newsletter: [9,10,11,12,13],
      position: '',
      showSubPositions: false,
      hasAllergies: false,
      hasMedicalHistory: false,
      hasMedicalStaff: false,
      gunForm: 0
    }
  },
  mounted() {
    // this.$refs.subPositions.value = ''

    setTimeout(() => {
      console.log(this.$refs.position_value.value)
      this.position = this.$refs.position_value.value != 'None' ? this.$refs.position_value.value : ''
    }, 100);
  },

  methods: {
    showAllOptions(options) {
      options.forEach((option) => {
        option.style.display = 'block'
      })
    },
    displaySubPositions(position) {
      if([2, 11, 14, 15, 16].includes(parseInt(position))) {
        this.showSubPositions = true
      } else {
        this.showSubPositions = false
      }
    },

    saveInternationalForm() {
      let form = document.getElementById('international-form')
      let formData = new FormData(form)

      axios.post('/international-form/', formData)
        .then((response) => {
          console.log(response)
          location.reload()
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  watch: {
    position(position) {
      this.displaySubPositions(position)
      let options = Array.from(this.$refs.subPositions.options)

      this.showAllOptions(options)
      this.showMediaChannels = false
      this.gunForm = 0

      switch (position) {
        case '2':
          options.forEach((option) => {
            if(!this.headOfDelegations.includes(parseInt(option.value))) {
              option.style.display = 'none'
            }
          })
          break
        case '10':
          this.gunForm += 1
          break
        case '11':
          options.forEach((option) => {
            if(!this.suppliers.includes(parseInt(option.value))) {
              option.style.display = 'none'
            }
          })
          break
        case '14':
        case '15':
        case '16':
          options.forEach((option) => {
            if(!this.newsletter.includes(parseInt(option.value))) {
              option.style.display = 'none'
            }

            this.showMediaChannels = true
          })
          break

      }
    }
  }
}).mount('#national_form_app')
