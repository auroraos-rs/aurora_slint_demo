slint::include_modules!();

fn main() -> Result<(), slint::PlatformError> {
    std::env::set_var(
        "SLINT_DEBUG_PERFORMANCE",
        "refresh_full_speed,overlay,console",
    );
    std::env::set_var("SLINT_SCALE_FACTOR", "2.0");

    let ui = AppWindow::new()?;
    ui.run()
}
