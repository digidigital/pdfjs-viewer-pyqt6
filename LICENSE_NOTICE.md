# License Notice for pdfjs-viewer-pyqt6

## Module License

This module (`pdfjs-viewer-pyqt6`) is licensed under the **GNU General Public License v3.0 or later (GPL-3.0-or-later)**.

See the [LICENSE](LICENSE) file for the full GPL v3.0 license text.

## PyQt6 Dependency Notice

**This module uses PyQt6, which is licensed under the GPL v3.**

### GPL Requirements

Since this module depends on PyQt6 (which is GPL-licensed), this module must also be distributed under the GPL v3.

**Important:** Applications that use this module are considered derivative works and must also be licensed under the GPL v3 or a compatible license.

### GPL Implications for Application Developers

If you distribute an application that uses this module:

1. ⚠️ **Your entire application must be GPL-licensed** (or GPL-compatible)
2. ✅ **You must provide source code** of your application to users
3. ✅ **Include the GPL v3 license text** (see [LICENSE](LICENSE))
4. ✅ **Preserve all copyright notices** and license information

### Alternative: Use pdfjs-viewer-pyside6 Instead

If you want to distribute a proprietary (closed-source) application:

**Use `pdfjs-viewer-pyside6` instead of this package.**

- `pdfjs-viewer-pyside6` uses PySide6 (LGPL-licensed)
- LGPL allows use in proprietary applications without requiring you to open-source your application
- The API is identical between both packages

Install the LGPL-licensed alternative:
```bash
pip install pdfjs-viewer-pyside6
```

Then simply change your imports:
```python
# Change this:
from pdfjs_viewer import PDFViewerWidget

# No code changes needed - API is identical!
```

## PyQt6 vs PySide6 Licensing Summary

| Package | Qt Binding | License | Proprietary Use |
|---------|-----------|---------|----------------|
| `pdfjs-viewer-pyqt6` | PyQt6 | **GPL v3** | ❌ No - must open-source your app |
| `pdfjs-viewer-pyside6` | PySide6 | **LGPL v3** | ✅ Yes - keep libraries external |

## Other Dependencies

This module also uses:

- **PDF.js** - Apache License 2.0 (bundled, see `src/pdfjs_viewer/pdfjs/LICENSE`)

## Questions?

This notice is provided to the best of our knowledge but is **NOT legal advice**.

If you're unsure about license compliance for your specific use case, please consult with a legal professional or licensing expert.

## Additional Resources

- [GPL v3.0 Full Text](https://www.gnu.org/licenses/gpl-3.0.html)
- [PyQt6 Licensing](https://www.riverbankcomputing.com/commercial/license-faq)
- [Choosing Between GPL and LGPL](https://www.gnu.org/licenses/gpl-faq.html)
- [Why PySide6 Uses LGPL](https://www.qt.io/blog/qt-for-python)
