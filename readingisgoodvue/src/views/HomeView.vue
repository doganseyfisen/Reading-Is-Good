<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to Reading Is Good...
        </p>
        <p>
          An online books retail firm
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest books</h2>
      </div>

      <BookBox v-for="book in latestBooks" v-bind:key="book.id" v-bind:book="book"/>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import BookBox from '@/components/BookBox'

export default {
  name: 'HomeView',
  data() {
    return {
      latestBooks: []
    }
  },
  components: {
    BookBox
  },
  mounted() {
    this.getLatestBooks()
    
    document.title = 'Home | Reading Is Good'
  },
  methods: {
    async getLatestBooks() {
      this.$store.commit('setIsLoading', true)

      /**
       * Axios
       */
      await axios
        .get('/api/v1/latest-books/')
        .then(response => {
          this.latestBooks = response.data
        })
        .catch(error => {
          console.log(error)
        })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>
