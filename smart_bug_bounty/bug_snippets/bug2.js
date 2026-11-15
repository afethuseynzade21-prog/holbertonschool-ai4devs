// Load several users in parallel and return them in the same order as `ids`.
async function loadUsers(ids, fetchUser) {
  const users = [];

  ids.forEach(async (id) => {
    const user = await fetchUser(id);
    users.push(user);
  });

  return users;
}

// Fake fetch function used for a quick manual test.
const fakeFetch = (id) =>
  new Promise((resolve) => setTimeout(() => resolve({ id }), 10));

loadUsers([1, 2, 3], fakeFetch).then((users) => {
  console.log(users); // expected: [ { id: 1 }, { id: 2 }, { id: 3 } ]
});

module.exports = loadUsers;
