// Load several users in parallel and return them in the same order as `ids`.
async function loadUsers(ids, fetchUser) {
  // Fix: wait for every request. Promise.all keeps the order of `ids`.
  return Promise.all(ids.map((id) => fetchUser(id)));
}

module.exports = loadUsers;

if (require.main === module) {
  // Fake fetch function used for a quick manual test.
  const fakeFetch = (id) =>
    new Promise((resolve) => setTimeout(() => resolve({ id }), 10));

  loadUsers([1, 2, 3], fakeFetch).then((users) => {
    console.log(users); // expected: [ { id: 1 }, { id: 2 }, { id: 3 } ]
  });
}
