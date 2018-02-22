<template>
  <div>
    <ul v-if="users && users.length">
      <li v-for="user of users">
        <p><strong>Name: {{user.name}}</strong></p>
        <p>ID: {{user.id}}</p>
      </li>
    </ul>
    <ul v-if="errors && errors.length">
      <h2> {{errors.length}} error(s) occured: </h2>
      <li v-for="error of errors">
        <p><strong>{{error.name}}</strong></p>
        <p>{{error.message}}</p>
      </li>
    </ul>
  </div>
</template>

<script>

// import axios from 'axios'

export default {
  data () {
    return {
      users: [],
      errors: []
    }
  },

  created () {
    // axios.get('http://zeus.ugent.be/allUsers')
    // .then(response => {
    //   this.users = response.users
    // })
    // .catch(err => {
    //   this.errors.push(err)
    // })

    this.users = [
      {
        name: 'Persoon 1',
        id: 'P1'
      },
      {
        name: 'Persoon 2',
        id: 'P2'
      },
      {
        name: 'Persoon 3',
        id: 'P3'
      }
    ]

    this.errors.push({
      name: 'Very bad error',
      message: 'Not actually bad'
    })
    this.errors.push({
      name: 'Not really an error',
      message: 'It\'s a feature'
    })
  }
}
</script>
