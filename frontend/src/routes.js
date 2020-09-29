import Home from './views/Home';
import Register from './views/user-views/Register';
import Login from './views/user-views/Login';
import MovieDetail from './components/layouts/MovieDetail';
import Logout from './views/user-views/Logout';
import NotFound from './views/NotFound';

export const routes = [
    {
        path : '',
        component : Home,
        name:'home'
    },
    {
        path : '/register',
        component: Register
    },
    {
        name : 'login',
        path : '/login',
        component: Login
    },
    {
        path : '/detail/:slug',
        component: MovieDetail,
        name : 'detail'
    },
    {
        path : '/logout',
        component: Logout,
        name : 'logout'
    },
    {
        path : '*',
        component: NotFound,
        name : '404-page'
    }
]