/**
 * Created Search.vue
 */

<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Search</h1>
                <h2 class="is-size-5 has-text-grey">Search term: "{{ query }}"</h2>
            </div>

            <BookBox v-for="book in books" v-bind:key="book.id" v-bind:book="book"/>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import BookBox from '@/components/BookBox.vue'

export default {
    name: 'Search',
    data() {
        return {
            books: [],
            query: ''
        }
    },
    components: {
        BookBox
    },
    mounted() {
        document.title = 'Search | Reading Is Good'

        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')) {
            this.query = params.get('query')
            this.performSearch()
        }
    },
    methods: {
        async performSearch() {
            this.$store.commit('setIsLoading', true)

            await axios
                .post('/api/v1/books/search/', {'query': this.query})
                .then(response => {
                    this.books = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>