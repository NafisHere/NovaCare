# TODO - NovaCare fixes & theme overhaul

## Step 1: Auth fixes
- [ ] Update `app.py` logout routes (`/logout`, `/other_logout`) to redirect to `/` (home) instead of login pages.
- [ ] Update `app.py` `/other_register` and `/register` duplicate-email handling to show “already have an account? Login” UX (no confusing redirects).

## Step 2: Navbar/UX fixes
- [ ] Update `templates/home.html`: change branding to **NovaCare Hospital**.
- [ ] Add doctor/admin/pharmacist **Register** button on home navbar linking to `/other_register`.
- [ ] Update `templates/dashboard.html` (and any other shared nav) so logged-in users do NOT see “Login”, only “Logout”.

## Step 3: Visual theme foundations
- [ ] Add favicon in `templates/home.html` (use `static/images/ho.png`).
- [ ] Create new global stylesheet `static/theme.css` with dark animated gradient theme.
- [ ] Update `home.html` to use the new theme and animated styling.

## Step 4: Home page redesign
- [ ] Home logo top-left using `static/images/hosp.png` with hover animation and click to `/`.
- [ ] Update hero/slider images order: `hos4 → hos3 → hos5 → hos7 → hos6 → desh2 → med`.
- [ ] Add hover/scale effect on slider images.
- [ ] Update hospital description text to exactly match the provided text, with vibrant animated typography.

## Step 5: Footer & branding everywhere
- [ ] Replace “AIMS Hospital” with “NovaCare Hospital” across templates that contain it.
- [ ] Add footer text everywhere: `@2026 All rights reserved to NovaCare Hospital`.
- [ ] Ensure logout buttons still work and route to `/`.

## Step 6: Verify & test
- [ ] Start server and test flows for patient/doctor/admin/pharmacist:
  - logout → home
  - home navbar login/register visibility
  - register-with-existing-email shows login link
- [ ] Validate no broken assets (favicon/logo/slider images).

