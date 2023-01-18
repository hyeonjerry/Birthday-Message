<script>
  import Router from "svelte-spa-router";
  import Home from "./routes/Home.svelte";
  import UserLogin from "./routes/UserLogin.svelte";

  const routes = {
    "/": Home,
    "/user-login": UserLogin,
  };
</script>

<Router {routes} />
