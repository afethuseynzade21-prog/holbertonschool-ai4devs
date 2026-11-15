class Bug3 {
    // Return true when the given role is exactly "admin".
    static boolean isAdmin(String role) {
        if (role == "admin") {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        String literalRole = "admin";
        String typedRole = new String("admin"); // for example, read from user input

        System.out.println(isAdmin(literalRole)); // expected: true
        System.out.println(isAdmin(typedRole));   // expected: true
        System.out.println(isAdmin("user"));      // expected: false
    }
}
