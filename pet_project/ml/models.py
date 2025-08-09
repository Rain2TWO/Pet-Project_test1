"""Base classes for machine learning models."""

from __future__ import annotations
from typing import Any


class BaseModel:
    """Abstract base class for ML models."""

    def train(self, data: Any) -> None:
        """Train the model on the provided data."""
        raise NotImplementedError

    def predict(self, data: Any) -> Any:
        """Generate predictions for the provided data."""
        raise NotImplementedError
