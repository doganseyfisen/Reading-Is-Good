/**
 * Created Category.vue
 */

<template>
    <div class="page-category">
        <div class="columns is-multiline">
            <h2 class="is-size-2 has-text-centered">{{ category.name }}</h2>
        </div>

        <BookBox v-for="book in category.books" v-bind:key="book.id" v-bind:book="book"/>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import BookBox from '@/components/BookBox.vue'

export default {
    name: 'Category',
    data() {
        return {
            category: {
                books: []
            }
        }
    },
    components: {
        BookBox
    },
    mounted() {
        this.getCategory()
    },
    watch: {
        $route(to, from) {
            if (to.name === 'Category') {
                this.getCategory()
            }
        }
    },
    methods: {
        async getCategory() {
            const categorySlug = this.$route.params.category_slug

            this.$store.commit('selfIsLoading', true)

            axios
                .get(`/api/v1/books/${categorySlug}/`)
                .then(response => {
                    this.category = response.data

                    document.title = this.category.name + ' | Reading Is Good'
                })
                .catch(error => {
                    console.log(error)

                    toast({
                        message: 'Something went wrong, try again.',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                })

            this.$store.commit('selfIsLoading', false)
        }
    }
}
</script>