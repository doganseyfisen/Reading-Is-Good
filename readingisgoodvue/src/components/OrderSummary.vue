/**
 * Created OrderSummary.vue   
 */

<template>
    <div class="box mb-4">
        <h3 class="is-size-4 mb-6">Order #{{ order.id }}</h3>

        <h4 class="is-size-5">Books</h4>

        <table class="table is-fullwidth">
            <thead>
                <tr>
                    <th>Book</th>
                    <th>Price</th>
                    <th>Quantity</th>
                    <th>Total</th>
                </tr>
            </thead>

            <tbody>
                <tr v-for="item in order.items" v-bind:key="item.book.id">
                    <td>{{ item.book.name }}</td>
                    <td>${{ item.book.price }}</td>
                    <td>{{ item.quantity }}</td>
                    <td>${{ getItemTotal(item).toFixed(2) }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: 'OrderSummary',
    props: {
        order: Object
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.book.price
        },
        orderTotalLength(order) {
            return order.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
    }
}
</script>