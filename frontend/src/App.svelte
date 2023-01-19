<script>
  import Router from "svelte-spa-router";
  import Home from "./routes/Home.svelte";
  import UserLogin from "./routes/UserLogin.svelte";
  import MyPage from "./routes/MyPage.svelte";
  import BirthdayDetail from "./routes/BirthdayDetail.svelte";
  import BirthdayCreate from "./routes/BirthdayCreate.svelte";
  import UserCreate from "./routes/UserCreate.svelte";

  const routes = {
    "/": Home,
    "/user-login": UserLogin,
    "/user-create": UserCreate,
    "/my-page": MyPage,
    "/birthday-detail/:birthday_id": BirthdayDetail,
    "/create-birthday": BirthdayCreate,
  };
</script>

<Router {routes} />
