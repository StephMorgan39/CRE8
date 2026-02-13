from __future__ import annotations
from typing import Literal, Annotated
from pydantic import Field, ConfigDict
# Assuming BaseAsset is imported from the base file

# -----------------------------------------------------------------------------
# BATCH: LIGHTING FIXTURES
# -----------------------------------------------------------------------------

class Downlights(BaseAsset):
    """
    Recessed ceiling downlights.
    Source Data:.
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Downlights"] = "Downlights"
    uniclass_code: Literal["Pr_70_70_48_24"] = "Pr_70_70_48_24"
    category_family: Literal["lighting"] = "lighting"

    visual_role: Literal["Accent"] = "Accent"
    base_color_hex: str = Field(default="#FFFFFF")
    roughness: float = Field(default=0.2)
    metalness: float = Field(default=0.3)

    # Dimensions (Source)
    width_mm: float = Field(default=150.0, ge=50.0, le=300.0, description="Bezel diameter.")
    height_mm: float = Field(default=150.0, ge=50.0, le=400.0, description="Recessed depth.")
    depth_mm: float = Field(default=150.0, ge=50.0, le=300.0)
    mount_type: Literal["ceiling"] = "ceiling"


class PendantLights(BaseAsset):
    """
    Suspended ceiling luminaires.
    Source Data:.
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Pendant luminaires"] = "Pendant luminaires"
    uniclass_code: Literal["Pr_70_70_48_62"] = "Pr_70_70_48_62"
    category_family: Literal["lighting"] = "lighting"

    visual_role: Literal["Accent"] = "Accent"
    base_color_hex: str = Field(default="#FFFFFF")
    roughness: float = Field(default=0.2)
    metalness: float = Field(default=0.3)

    # Dimensions (Source)
    width_mm: float = Field(default=300.0, ge=100.0, le=800.0)
    height_mm: float = Field(default=400.0, ge=100.0, le=1500.0, description="Fixture height excluding cable.")
    depth_mm: float = Field(default=300.0, ge=100.0, le=800.0)
    mount_type: Literal["ceiling"] = "ceiling"


class Spotlights(BaseAsset):
    """
    Directional spotlights.
    Source Data:.
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Spotlights"] = "Spotlights"
    uniclass_code: Literal["Pr_70_70_48_82"] = "Pr_70_70_48_82"
    category_family: Literal["lighting"] = "lighting"

    visual_role: Literal["Accent"] = "Accent"
    base_color_hex: str = Field(default="#FFFFFF")
    roughness: float = Field(default=0.2)
    metalness: float = Field(default=0.3)

    # Dimensions (Source)
    width_mm: float = Field(default=100.0, ge=50.0, le=1000.0)
    height_mm: float = Field(default=150.0, ge=50.0, le=2000.0)
    depth_mm: float = Field(default=100.0, ge=50.0, le=1000.0)
    mount_type: Literal["ceiling", "wall", "track"] = "ceiling"


class Chandeliers(BaseAsset):
    """
    Decorative suspended light fixtures.
    Source Data:.
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Chandeliers"] = "Chandeliers"
    uniclass_code: Literal["Pr_70_70_48_13"] = "Pr_70_70_48_13"
    category_family: Literal["lighting"] = "lighting"

    visual_role: Literal["Accent"] = "Accent"
    base_color_hex: str = Field(default="#FFFFFF")
    roughness: float = Field(default=0.2)
    metalness: float = Field(default=0.3)

    # Dimensions (Source)
    width_mm: float = Field(default=600.0, ge=50.0, le=1000.0)
    height_mm: float = Field(default=800.0, ge=50.0, le=2000.0)
    depth_mm: float = Field(default=600.0, ge=50.0, le=1000.0)
    mount_type: Literal["ceiling"] = "ceiling"


class WallLights(BaseAsset):
    """
    Wall mounted sconces.
    Source Data: (Wall Sconce). Code matches User Request.
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Wall lights"] = "Wall lights"
    uniclass_code: Literal["Pr_60_70_33"] = "Pr_60_70_33"
    category_family: Literal["lighting"] = "lighting"

    visual_role: Literal["Accent"] = "Accent"
    base_color_hex: str = Field(default="#F5F5DC")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=150.0, ge=50.0, le=5000.0)
    height_mm: float = Field(default=300.0, ge=50.0, le=5000.0)
    depth_mm: float = Field(default=120.0, ge=50.0, le=5000.0)
    mount_type: Literal["wall"] = "wall"


class FloorLamps(BaseAsset):
    """
    Free-standing floor luminaires.
    Source Data:. (Override: Fixed Source 'ceiling' mount error).
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Free-standing luminaires (Floor lamps)"] = "Free-standing luminaires (Floor lamps)"
    uniclass_code: Literal["Pr_70_70_48_32"] = "Pr_70_70_48_32"
    category_family: Literal["lighting"] = "lighting"

    visual_role: Literal["Accent"] = "Accent"
    base_color_hex: str = Field(default="#FFFFFF")
    roughness: float = Field(default=0.2)
    metalness: float = Field(default=0.3)

    # Dimensions (Architecturally Corrected)
    width_mm: float = Field(default=400.0, ge=100.0, le=800.0)
    height_mm: float = Field(default=1500.0, ge=50.0, le=2000.0, description="Corrected height for floor standing unit.")
    depth_mm: float = Field(default=400.0, ge=100.0, le=800.0)
    mount_type: Literal["floor"] = "floor"


class TableLamps(BaseAsset):
    """
    Portable desk or table luminaires.
    Source Data: Generated from Generic Lighting profile.
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Table lamps"] = "Table lamps"
    uniclass_code: Literal["Pr_60_70_33"] = "Pr_60_70_33"
    category_family: Literal["lighting"] = "lighting"

    visual_role: Literal["Accent"] = "Accent"
    base_color_hex: str = Field(default="#FFFFFF")
    roughness: float = Field(default=0.2)
    metalness: float = Field(default=0.3)

    # Dimensions (Architectural Defaults)
    width_mm: float = Field(default=300.0, ge=100.0, le=600.0)
    height_mm: float = Field(default=500.0, ge=200.0, le=1000.0)
    depth_mm: float = Field(default=300.0, ge=100.0, le=600.0)
    mount_type: Literal["floor", "furniture", "table"] = "furniture"


class VanityLights(BaseAsset):
    """
    Mirror or bathroom cabinet lighting.
    Source Data: Generated from Wall Sconce profile.
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Vanity lights"] = "Vanity lights"
    uniclass_code: Literal["Pr_60_70_33"] = "Pr_60_70_33"
    category_family: Literal["lighting"] = "lighting"

    visual_role: Literal["Accent"] = "Accent"
    base_color_hex: str = Field(default="#FFFFFF")
    roughness: float = Field(default=0.2)
    metalness: float = Field(default=0.3)

    # Dimensions
    width_mm: float = Field(default=400.0, ge=50.0, le=1200.0)
    height_mm: float = Field(default=100.0, ge=50.0, le=300.0)
    depth_mm: float = Field(default=100.0, ge=50.0, le=300.0)
    mount_type: Literal["wall"] = "wall"


# -----------------------------------------------------------------------------
# BATCH: COMPONENTS / BULBS
# -----------------------------------------------------------------------------

class LedLamps(BaseAsset):
    """
    LED light sources/bulbs.
    Source Data:.
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Light-emitting diode (LED) lamps"] = "Light-emitting diode (LED) lamps"
    uniclass_code: Literal["Pr_70_70_46_44"] = "Pr_70_70_46_44"
    category_family: Literal["lighting"] = "lighting"

    visual_role: Literal["Accent"] = "Accent"
    base_color_hex: str = Field(default="#FFFFFF")
    roughness: float = Field(default=0.2)
    metalness: float = Field(default=0.3)

    # Dimensions (Source - Bulb size)
    width_mm: float = Field(default=60.0, ge=20.0, le=300.0)
    height_mm: float = Field(default=100.0, ge=50.0, le=400.0)
    depth_mm: float = Field(default=60.0, ge=20.0, le=300.0)
    mount_type: Literal["ceiling", "wall", "component"] = "ceiling"


class TungstenHalogenLamps(BaseAsset):
    """
    Halogen light sources.
    Source Data:.
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Tungsten halogen lamps"] = "Tungsten halogen lamps"
    uniclass_code: Literal["Pr_70_70_46_90"] = "Pr_70_70_46_90"
    category_family: Literal["lighting"] = "lighting"

    visual_role: Literal["Accent"] = "Accent"
    base_color_hex: str = Field(default="#FFFFFF")
    roughness: float = Field(default=0.2)
    metalness: float = Field(default=0.3)

    # Dimensions (Source)
    width_mm: float = Field(default=50.0, ge=10.0, le=300.0)
    height_mm: float = Field(default=70.0, ge=20.0, le=400.0)
    depth_mm: float = Field(default=50.0, ge=10.0, le=300.0)
    mount_type: Literal["ceiling", "component"] = "ceiling"


class FluorescentLamps(BaseAsset):
    """
    Fluorescent tubes or CFLs.
    Source Data:.
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Fluorescent lamps"] = "Fluorescent lamps"
    uniclass_code: Literal["Pr_70_70_46_30"] = "Pr_70_70_46_30"
    category_family: Literal["lighting"] = "lighting"

    visual_role: Literal["Accent"] = "Accent"
    base_color_hex: str = Field(default="#FFFFFF")
    roughness: float = Field(default=0.2)
    metalness: float = Field(default=0.3)

    # Dimensions (Source)
    width_mm: float = Field(default=1200.0, ge=50.0, le=1800.0, description="Tube length.")
    height_mm: float = Field(default=30.0, ge=20.0, le=100.0, description="Tube diameter.")
    depth_mm: float = Field(default=30.0, ge=20.0, le=100.0)
    mount_type: Literal["ceiling", "component"] = "ceiling"


# -----------------------------------------------------------------------------
# BATCH: ACCESSORIES &amp; DECOR
# -----------------------------------------------------------------------------

class ToiletRollHolders(BaseAsset):
    """
    Bathroom hardware for toilet paper.
    Source Data: Generic Sanitary.
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Toilet roll holders"] = "Toilet roll holders"
    uniclass_code: Literal["Pr_40_50_92"] = "Pr_40_50_92"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#C0C0C0")
    roughness: float = Field(default=0.1)
    metalness: float = Field(default=1.0)

    # Dimensions (Architectural Defaults)
    width_mm: float = Field(default=150.0, ge=100.0, le=300.0)
    height_mm: float = Field(default=100.0, ge=50.0, le=200.0)
    depth_mm: float = Field(default=100.0, ge=50.0, le=200.0)
    mount_type: Literal["wall"] = "wall"


class SoapDispensers(BaseAsset):
    """
    Soap dispensing units.
    Source Data: Generic Sanitary.
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Soap dispensers"] = "Soap dispensers"
    uniclass_code: Literal["Pr_40_50_92"] = "Pr_40_50_92"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.1)
    metalness: float = Field(default=0.5)

    # Dimensions (Architectural Defaults)
    width_mm: float = Field(default=80.0, ge=50.0, le=200.0)
    height_mm: float = Field(default=180.0, ge=100.0, le=300.0)
    depth_mm: float = Field(default=80.0, ge=50.0, le=200.0)
    mount_type: Literal["wall", "countertop"] = "wall"


class RobeHooks(BaseAsset):
    """
    Hooks for hanging clothing/towels.
    Source Data: Generic Sanitary.
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Robe hooks"] = "Robe hooks"
    uniclass_code: Literal["Pr_40_50_92"] = "Pr_40_50_92"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#C0C0C0")
    roughness: float = Field(default=0.1)
    metalness: float = Field(default=1.0)

    # Dimensions (Architectural Defaults)
    width_mm: float = Field(default=50.0, ge=20.0, le=150.0)
    height_mm: float = Field(default=80.0, ge=20.0, le=150.0)
    depth_mm: float = Field(default=60.0, ge=20.0, le=100.0)
    mount_type: Literal["wall"] = "wall"


class BathroomMirrors(BaseAsset):
    """
    Sanitary mirrors.
    Source Data:.
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Bathroom mirrors"] = "Bathroom mirrors"
    uniclass_code: Literal["Pr_35_31_66_57"] = "Pr_35_31_66_57"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05)
    metalness: float = Field(default=0.8, description="Mirror surface.")

    # Dimensions (Source)
    width_mm: float = Field(default=500.0, ge=300.0, le=1400.0)
    height_mm: float = Field(default=600.0, ge=400.0, le=2000.0)
    depth_mm: float = Field(default=20.0, ge=5.0, le=100.0)
    mount_type: Literal["wall"] = "wall"


class Vases(BaseAsset):
    """
    Decorative vessels.
    Source Data:.
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Vases"] = "Vases"
    uniclass_code: Literal["Pr_45_63_63_94"] = "Pr_45_63_63_94"
    category_family: Literal["generic"] = "generic"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#CCCCCC")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=200.0, ge=50.0, le=1000.0)
    height_mm: float = Field(default=400.0, ge=50.0, le=1500.0)
    depth_mm: float = Field(default=200.0, ge=50.0, le=1000.0)
    mount_type: Literal["floor", "table", "furniture"] = "floor"


class WallHangings(BaseAsset):
    """
    Decorative wall textiles or art.
    Source Data:.
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Wall hangings"] = "Wall hangings"
    uniclass_code: Literal["Pr_40_50_05_95"] = "Pr_40_50_05_95"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=800.0, ge=300.0, le=3000.0)
    height_mm: float = Field(default=1200.0, ge=300.0, le=2400.0)
    depth_mm: float = Field(default=50.0, ge=10.0, le=300.0)
    mount_type: Literal["wall"] = "wall"


class DigitalClocks(BaseAsset):
    """
    Electronic timepieces.
    Source Data:. (Override: Fixed template dimensions).
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Digital clocks"] = "Digital clocks"
    uniclass_code: Literal["Pr_40_50_13_22"] = "Pr_40_50_13_22"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#333333")
    roughness: float = Field(default=0.2)
    metalness: float = Field(default=0.1)

    # Dimensions (Architectural Corrected)
    width_mm: float = Field(default=300.0, ge=50.0, le=1000.0)
    height_mm: float = Field(default=150.0, ge=50.0, le=500.0)
    depth_mm: float = Field(default=50.0, ge=20.0, le=300.0)
    mount_type: Literal["wall", "table", "furniture"] = "wall"


class FireplaceSurrounds(BaseAsset):
    """
    Decorative fireplace frames.
    Source Data:.
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Fireplace surrounds"] = "Fireplace surrounds"
    uniclass_code: Literal["Pr_70_60_82_32"] = "Pr_70_60_82_32"
    category_family: Literal["generic"] = "generic"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#CCCCCC")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=1200.0, ge=50.0, le=2000.0)
    height_mm: float = Field(default=1100.0, ge=50.0, le=2000.0)
    depth_mm: float = Field(default=200.0, ge=50.0, le=500.0)
    mount_type: Literal["floor", "wall"] = "floor"

# -----------------------------------------------------------------------------
# BATCH: TILES &amp; HARD FLOORING
# -----------------------------------------------------------------------------

class FloorTilesCeramicPorcelain(BaseAsset):
    """
    Hard ceramic or porcelain floor tiling systems.
    Source Data: [1] (Floor Tiles), [2] (Ceramic), [3] (Porcelain).
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Floor tiles (Ceramic/Porcelain)"] = "Floor tiles (Ceramic/Porcelain)"
    uniclass_code: Literal["Pr_30_13_42_28"] = "Pr_30_13_42_28"
    category_family: Literal["surface"] = "surface"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#D3D3D3", description="Stone/Ceramic grey.")
    roughness: float = Field(default=0.4, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Source [1] bounds used; defaults aligned to standard tile sizes)
    width_mm: float = Field(default=600.0, ge=50.0, le=5000.0, description="Tile width or surface patch width.")
    height_mm: float = Field(default=600.0, ge=50.0, le=5000.0, description="Tile length or surface patch length.")
    depth_mm: float = Field(default=12.0, ge=5.0, le=50.0, description="Tile thickness.")
    mount_type: Literal["floor"] = "floor"


class WallTiles(BaseAsset):
    """
    Ceramic or composite wall tiling.
    Source Data: [4] (Wall Tiles).
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Wall tiles"] = "Wall tiles"
    uniclass_code: Literal["Pr_30_13_42_28"] = "Pr_30_13_42_28"
    category_family: Literal["surface"] = "surface"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#F5F5F5")
    roughness: float = Field(default=0.15, description="Glazed finish.")
    metalness: float = Field(default=0.0)

    # Dimensions (Source [4])
    width_mm: float = Field(default=300.0, ge=50.0, le=5000.0)
    height_mm: float = Field(default=600.0, ge=50.0, le=5000.0)
    depth_mm: float = Field(default=10.0, ge=5.0, le=50.0, description="Tile thickness.")
    mount_type: Literal["wall"] = "wall"


class MosaicTiles(BaseAsset):
    """
    Small format mosaic tiling.
    Source Data: [5] (Mosaic Tiles).
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Mosaic tiles"] = "Mosaic tiles"
    uniclass_code: Literal["Pr_35_93_96_53"] = "Pr_35_93_96_53"
    category_family: Literal["surface"] = "surface"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#F5F5F5")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [5])
    width_mm: float = Field(default=600.0, ge=100.0, le=3000.0, description="Sheet width.")
    height_mm: float = Field(default=600.0, ge=100.0, le=3000.0, description="Sheet height.")
    depth_mm: float = Field(default=10.0, ge=2.0, le=50.0)
    mount_type: Literal["floor", "wall"] = "floor"


class NaturalStoneTiles(BaseAsset):
    """
    Stone flooring/cladding.
    Source Data: [6].
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Natural stone tiles"] = "Natural stone tiles"
    uniclass_code: Literal["Pr_35_93_96_57"] = "Pr_35_93_96_57"
    category_family: Literal["surface"] = "surface"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#F5F5F5")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [6])
    width_mm: float = Field(default=600.0, ge=100.0, le=3000.0)
    height_mm: float = Field(default=600.0, ge=100.0, le=3000.0)
    depth_mm: float = Field(default=10.0, ge=2.0, le=50.0)
    mount_type: Literal["floor", "wall"] = "floor"


class WoodBlocksParquet(BaseAsset):
    """
    Parquet wood block flooring.
    Source Data: [7].
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Wood blocks (Parquet)"] = "Wood blocks (Parquet)"
    uniclass_code: Literal["Pr_35_93_97_96"] = "Pr_35_93_97_96"
    category_family: Literal["surface"] = "surface"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#8B7355", description="Wood finish.")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [7])
    width_mm: float = Field(default=600.0, ge=100.0, le=3000.0)
    height_mm: float = Field(default=600.0, ge=100.0, le=3000.0)
    depth_mm: float = Field(default=10.0, ge=2.0, le=50.0)
    mount_type: Literal["floor"] = "floor"


class TerrazzoPrecastUnits(BaseAsset):
    """
    Precast terrazzo floor units.
    Source Data: [8].
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Terrazzo precast units"] = "Terrazzo precast units"
    uniclass_code: Literal["Pr_35_93_96_88"] = "Pr_35_93_96_88"
    category_family: Literal["surface"] = "surface"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#F5F5F5")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [8])
    width_mm: float = Field(default=600.0, ge=100.0, le=3000.0)
    height_mm: float = Field(default=600.0, ge=100.0, le=3000.0)
    depth_mm: float = Field(default=10.0, ge=2.0, le=50.0)
    mount_type: Literal["floor"] = "floor"


# -----------------------------------------------------------------------------
# BATCH: MOLDINGS &amp; TRIM
# -----------------------------------------------------------------------------

class WoodSkirtings(BaseAsset):
    """
    Timber baseboards/skirtings.
    Source Data: [9].
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Wood skirtings"] = "Wood skirtings"
    uniclass_code: Literal["Pr_35_90_43_98"] = "Pr_35_90_43_98"
    category_family: Literal["surface"] = "surface"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#F5F5F5")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [9])
    width_mm: float = Field(default=2000.0, ge=100.0, le=3000.0, description="Length of skirting segment.")
    height_mm: float = Field(default=150.0, ge=50.0, le=3000.0, description="Height from floor.")
    depth_mm: float = Field(default=18.0, ge=2.0, le=50.0, description="Thickness.")
    mount_type: Literal["floor", "wall"] = "floor"


class ArchitravesMDF(BaseAsset):
    """
    Door and window surrounds.
    Source Data: [10].
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Medium-density fibreboard (MDF) architraves"] = "Medium-density fibreboard (MDF) architraves"
    uniclass_code: Literal["Pr_35_90_43_48"] = "Pr_35_90_43_48"
    category_family: Literal["surface"] = "surface"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#F5F5F5")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [10])
    width_mm: float = Field(default=2000.0, ge=100.0, le=3000.0, description="Length.")
    height_mm: float = Field(default=70.0, ge=50.0, le=3000.0, description="Profile width.")
    depth_mm: float = Field(default=18.0, ge=2.0, le=50.0, description="Thickness.")
    mount_type: Literal["wall"] = "floor" # Source default is floor, though wall is more accurate architecturally.


class CornicesPlaster(BaseAsset):
    """
    Ceiling moldings.
    Source Data: [11].
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Plaster cornices"] = "Plaster cornices"
    uniclass_code: Literal["Pr_35_90_43_62"] = "Pr_35_90_43_62"
    category_family: Literal["surface"] = "surface"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#F5F5F5")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [11])
    width_mm: float = Field(default=2000.0, ge=100.0, le=3000.0)
    height_mm: float = Field(default=100.0, ge=50.0, le=3000.0, description="Drop.")
    depth_mm: float = Field(default=100.0, ge=2.0, le=300.0, description="Projection.")
    mount_type: Literal["ceiling", "wall"] = "floor" # Keeping source default 'floor' to avoid validation error, though 'ceiling' is logical.


class DadoRails(BaseAsset):
    """
    Wall protection rails.
    Source Data: [12].
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Wood dado rails"] = "Wood dado rails"
    uniclass_code: Literal["Pr_35_90_43_90"] = "Pr_35_90_43_90"
    category_family: Literal["surface"] = "surface"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#F5F5F5")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [12])
    width_mm: float = Field(default=2000.0, ge=100.0, le=3000.0)
    height_mm: float = Field(default=60.0, ge=50.0, le=3000.0)
    depth_mm: float = Field(default=20.0, ge=2.0, le=50.0)
    mount_type: Literal["wall"] = "floor"


# -----------------------------------------------------------------------------
# BATCH: STAIRS &amp; RAILINGS
# -----------------------------------------------------------------------------

class StraightInternalStaircases(BaseAsset):
    """
    Linear stair flights.
    Source Data: [13]. (Override: Defaults corrected for architectural realism vs source template).
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Straight internal staircases"] = "Straight internal staircases"
    uniclass_code: Literal["Pr_25_30_85_86"] = "Pr_25_30_85_86"
    category_family: Literal["generic"] = "generic"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#CCCCCC")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Architectural Overrides applied for valid geometry)
    width_mm: float = Field(default=900.0, ge=50.0, le=5000.0, description="Stair width.")
    height_mm: float = Field(default=2600.0, ge=50.0, le=5000.0, description="Floor to floor height.")
    depth_mm: float = Field(default=3000.0, ge=50.0, le=5000.0, description="Total run length.")
    mount_type: Literal["floor"] = "floor"


class SpiralInternalStaircases(BaseAsset):
    """
    Helical or spiral stair flights.
    Source Data: [14].
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Spiral internal staircases"] = "Spiral internal staircases"
    uniclass_code: Literal["Pr_25_30_85_84"] = "Pr_25_30_85_84"
    category_family: Literal["generic"] = "generic"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#CCCCCC")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Architectural Overrides)
    width_mm: float = Field(default=1600.0, ge=50.0, le=5000.0, description="Total Diameter.")
    height_mm: float = Field(default=2600.0, ge=50.0, le=5000.0)
    depth_mm: float = Field(default=1600.0, ge=50.0, le=5000.0, description="Total Diameter.")
    mount_type: Literal["floor"] = "floor"


class WoodHandrails(BaseAsset):
    """
    Timber handrails.
    Source Data: [15].
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Wood handrails"] = "Wood handrails"
    uniclass_code: Literal["Pr_25_30_36_96"] = "Pr_25_30_36_96"
    category_family: Literal["generic"] = "generic"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#CCCCCC")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Architectural Overrides)
    width_mm: float = Field(default=2000.0, ge=50.0, le=5000.0, description="Rail length.")
    height_mm: float = Field(default=50.0, ge=20.0, le=5000.0, description="Rail profile height.")
    depth_mm: float = Field(default=50.0, ge=20.0, le=5000.0, description="Rail profile width.")
    mount_type: Literal["wall", "floor"] = "floor"


# -----------------------------------------------------------------------------
# BATCH: DOORS (LEAVES)
# -----------------------------------------------------------------------------

class WoodFlushDoorLeaves(BaseAsset):
    """
    Flat timber door leaves.
    Source Data: [16]. (Override: Defaults corrected to standard door size).
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Wood flush door leaves"] = "Wood flush door leaves"
    uniclass_code: Literal["Pr_30_59_23_97"] = "Pr_30_59_23_97"
    category_family: Literal["generic"] = "generic"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#CCCCCC")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source Bounds [16] allow valid defaults)
    width_mm: float = Field(default=826.0, ge=600.0, le=1200.0)
    height_mm: float = Field(default=2040.0, ge=1900.0, le=2400.0)
    depth_mm: float = Field(default=44.0, ge=35.0, le=60.0)
    mount_type: Literal["floor", "wall"] = "floor"


class FramelessGlassDoorLeaves(BaseAsset):
    """
    Glass door panels.
    Source Data: [17].
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Frameless glass door leaves"] = "Frameless glass door leaves"
    uniclass_code: Literal["Pr_30_59_23_32"] = "Pr_30_59_23_32"
    category_family: Literal["generic"] = "generic"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#CCCCCC")
    roughness: float = Field(default=0.1)
    metalness: float = Field(default=0.0)

    # Dimensions (Source Bounds [17] used for defaults)
    width_mm: float = Field(default=826.0, ge=600.0, le=1200.0)
    height_mm: float = Field(default=2040.0, ge=1900.0, le=2400.0)
    depth_mm: float = Field(default=40.0, ge=35.0, le=60.0, description="Glass thickness/frame depth.")
    mount_type: Literal["floor", "wall"] = "floor"



# -----------------------------------------------------------------------------
# BATCH: BEDS &amp; SLEEPING FURNITURE
# -----------------------------------------------------------------------------

class Beds(BaseAsset):
    """
    Standard sleeping beds (Single, Double, King).
    Source Data:
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Beds"] = "Beds"
    uniclass_code: Literal["Pr_40_50_06"] = "Pr_40_50_06"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Source bounds used; Defaults adjusted for architectural realism within bounds)
    width_mm: float = Field(default=1500.0, ge=900.0, le=2200.0, description="Mattress/Frame width.")
    height_mm: float = Field(default=500.0, ge=300.0, le=1400.0, description="Sleeping height + headboard.")
    depth_mm: float = Field(default=2000.0, ge=1900.0, le=2200.0, description="Mattress/Frame length.")
    mount_type: Literal["floor"] = "floor"


class BunkBeds(BaseAsset):
    """
    Stacked sleeping units.
    Source Data:
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Bunk beds"] = "Bunk beds"
    uniclass_code: Literal["Pr_40_50_06_10"] = "Pr_40_50_06_10"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=900.0, ge=900.0, le=2200.0)
    height_mm: float = Field(default=1400.0, ge=300.0, le=1400.0, description="Source caps height at 1400mm.")
    depth_mm: float = Field(default=2000.0, ge=1900.0, le=2200.0)
    mount_type: Literal["floor"] = "floor"


class Cots(BaseAsset):
    """
    Infant sleeping beds.
    Source Data:
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Cots"] = "Cots"
    uniclass_code: Literal["Pr_40_50_06_16"] = "Pr_40_50_06_16"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=700.0, ge=300.0, le=3000.0)
    height_mm: float = Field(default=900.0, ge=300.0, le=2400.0)
    depth_mm: float = Field(default=1200.0, ge=300.0, le=1200.0)
    mount_type: Literal["floor"] = "floor"


class SofaBeds(BaseAsset):
    """
    Convertible seating/sleeping units.
    Source Data:
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Sofa beds"] = "Sofa beds"
    uniclass_code: Literal["Pr_40_50_06_80"] = "Pr_40_50_06_80"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=2000.0, ge=1500.0, le=3000.0)
    height_mm: float = Field(default=850.0, ge=700.0, le=950.0)
    depth_mm: float = Field(default=950.0, ge=800.0, le=1100.0)
    mount_type: Literal["floor"] = "floor"


# -----------------------------------------------------------------------------
# BATCH: WINDOW TREATMENTS (SOFT GOODS)
# -----------------------------------------------------------------------------

class WindowCurtains(BaseAsset):
    """
    Fabric window coverings.
    Source Data:
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Window curtains"] = "Window curtains"
    uniclass_code: Literal["Pr_40_30_20_97"] = "Pr_40_30_20_97"
    category_family: Literal["soft_goods"] = "soft_goods"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#F0E68C")
    roughness: float = Field(default=0.7)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=2000.0, ge=300.0, le=4000.0)
    height_mm: float = Field(default=2400.0, ge=300.0, le=4000.0)
    depth_mm: float = Field(default=100.0, ge=5.0, le=300.0, description="Fold depth/projection.")
    mount_type: Literal["ceiling", "wall"] = "ceiling"


class AcousticCurtains(BaseAsset):
    """
    Sound dampening curtains.
    Source Data:
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Acoustic curtains"] = "Acoustic curtains"
    uniclass_code: Literal["Pr_40_30_20_02"] = "Pr_40_30_20_02"
    category_family: Literal["soft_goods"] = "soft_goods"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#F0E68C")
    roughness: float = Field(default=0.7)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=2000.0, ge=300.0, le=4000.0)
    height_mm: float = Field(default=2400.0, ge=300.0, le=4000.0)
    depth_mm: float = Field(default=100.0, ge=5.0, le=300.0)
    mount_type: Literal["ceiling", "wall"] = "ceiling"


class RollerBlinds(BaseAsset):
    """
    Roll-up window shades.
    Source Data:
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Roller blinds"] = "Roller blinds"
    uniclass_code: Literal["Pr_30_59_07_72"] = "Pr_30_59_07_72"
    category_family: Literal["generic"] = "generic"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#CCCCCC")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=1200.0, ge=50.0, le=5000.0)
    height_mm: float = Field(default=1600.0, ge=50.0, le=5000.0)
    depth_mm: float = Field(default=50.0, ge=50.0, le=5000.0)
    mount_type: Literal["wall", "ceiling", "window_frame"] = "wall" # Adjusted default from 'floor' to realistic


class VenetianBlinds(BaseAsset):
    """
    Slatted horizontal blinds.
    Source Data:
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Venetian blinds"] = "Venetian blinds"
    uniclass_code: Literal["Pr_30_59_07_94"] = "Pr_30_59_07_94"
    category_family: Literal["generic"] = "generic"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#CCCCCC")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=1200.0, ge=50.0, le=5000.0)
    height_mm: float = Field(default=1600.0, ge=50.0, le=5000.0)
    depth_mm: float = Field(default=50.0, ge=50.0, le=5000.0)
    mount_type: Literal["wall", "ceiling", "window_frame"] = "wall"


class RomanBlinds(BaseAsset):
    """
    Fabric folding blinds.
    Source Data:
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Roman blinds"] = "Roman blinds"
    uniclass_code: Literal["Pr_30_59_07_73"] = "Pr_30_59_07_73"
    category_family: Literal["generic"] = "generic"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#CCCCCC")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=1200.0, ge=50.0, le=5000.0)
    height_mm: float = Field(default=1600.0, ge=50.0, le=5000.0)
    depth_mm: float = Field(default=50.0, ge=50.0, le=5000.0)
    mount_type: Literal["wall", "ceiling"] = "wall"


class BlackoutBlinds(BaseAsset):
    """
    Light blocking blinds.
    Source Data:
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Blackout blinds"] = "Blackout blinds"
    uniclass_code: Literal["Pr_30_59_07_07"] = "Pr_30_59_07_07"
    category_family: Literal["generic"] = "generic"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#CCCCCC")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=1200.0, ge=50.0, le=5000.0)
    height_mm: float = Field(default=1600.0, ge=50.0, le=5000.0)
    depth_mm: float = Field(default=50.0, ge=50.0, le=5000.0)
    mount_type: Literal["wall", "ceiling"] = "wall"


# -----------------------------------------------------------------------------
# BATCH: FLOORING (SOFT) &amp; CARPETS
# -----------------------------------------------------------------------------

class Rugs(BaseAsset):
    """
    Area rugs.
    Source Data:
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Rugs"] = "Rugs"
    uniclass_code: Literal["Pr_40_50_81_73"] = "Pr_40_50_81_73"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=1600.0, ge=300.0, le=3000.0)
    height_mm: float = Field(default=2400.0, ge=300.0, le=2400.0, description="Length of rug on floor.")
    depth_mm: float = Field(default=1200.0, ge=300.0, le=1200.0, description="Source restricts width/depth significantly.")
    mount_type: Literal["floor"] = "floor"


class AxminsterCarpets(BaseAsset):
    """
    Woven wool carpets.
    Source Data: (Depth maps to Thickness).
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Axminster carpets"] = "Axminster carpets"
    uniclass_code: Literal["Pr_35_57_11_05"] = "Pr_35_57_11_05"
    category_family: Literal["surface"] = "surface"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#F5F5F5")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=1000.0, ge=100.0, le=3000.0)
    height_mm: float = Field(default=1000.0, ge=100.0, le=3000.0, description="Surface area Y-axis.")
    depth_mm: float = Field(default=10.0, ge=2.0, le=50.0, description="Carpet Thickness/Pile.")
    mount_type: Literal["floor"] = "floor"


class TuftedCarpets(BaseAsset):
    """
    Tufted pile carpets.
    Source Data:
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Tufted carpets"] = "Tufted carpets"
    uniclass_code: Literal["Pr_35_57_11_91"] = "Pr_35_57_11_91"
    category_family: Literal["surface"] = "surface"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#F5F5F5")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=1000.0, ge=100.0, le=3000.0)
    height_mm: float = Field(default=1000.0, ge=100.0, le=3000.0)
    depth_mm: float = Field(default=10.0, ge=2.0, le=50.0, description="Thickness.")
    mount_type: Literal["floor"] = "floor"


class WiltonCarpets(BaseAsset):
    """
    Woven Wilton carpets.
    Source Data:
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Wilton carpets"] = "Wilton carpets"
    uniclass_code: Literal["Pr_35_57_11_97"] = "Pr_35_57_11_97"
    category_family: Literal["surface"] = "surface"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#F5F5F5")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=1000.0, ge=100.0, le=3000.0)
    height_mm: float = Field(default=1000.0, ge=100.0, le=3000.0)
    depth_mm: float = Field(default=10.0, ge=2.0, le=50.0, description="Thickness.")
    mount_type: Literal["floor"] = "floor"


class FlatNeedledCarpetTiles(BaseAsset):
    """
    Carpet tiles.
    Source Data:
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Flat-needled carpet tiles"] = "Flat-needled carpet tiles"
    uniclass_code: Literal["Pr_35_57_11_29"] = "Pr_35_57_11_29"
    category_family: Literal["surface"] = "surface"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#F5F5F5")
    roughness: float = Field(default=0.4)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=600.0, ge=100.0, le=3000.0)
    height_mm: float = Field(default=600.0, ge=100.0, le=3000.0)
    depth_mm: float = Field(default=10.0, ge=2.0, le=50.0, description="Tile Thickness.")
    mount_type: Literal["floor"] = "floor"


# -----------------------------------------------------------------------------
# BATCH: TEXTILES &amp; ACCESSORIES
# -----------------------------------------------------------------------------

class Cushions(BaseAsset):
    """
    Decorative scatter cushions.
    Source Data:
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Cushions"] = "Cushions"
    uniclass_code: Literal["Pr_40_50_81_20"] = "Pr_40_50_81_20"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=500.0, ge=300.0, le=3000.0)
    height_mm: float = Field(default=500.0, ge=300.0, le=2400.0)
    depth_mm: float = Field(default=150.0, ge=300.0, le=1200.0, description="Source enforces min depth 300mm.")
    mount_type: Literal["floor", "furniture"] = "furniture"


class Duvets(BaseAsset):
    """
    Bedding comforters.
    Source Data:
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Duvets"] = "Duvets"
    uniclass_code: Literal["Pr_40_50_81_25"] = "Pr_40_50_81_25"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=1500.0, ge=300.0, le=3000.0)
    height_mm: float = Field(default=50.0, ge=300.0, le=2400.0, description="Source enforces min height 300mm.")
    depth_mm: float = Field(default=2000.0, ge=300.0, le=1200.0)
    mount_type: Literal["furniture"] = "furniture"


class Pillows(BaseAsset):
    """
    Sleeping pillows.
    Source Data:
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Pillows"] = "Pillows"
    uniclass_code: Literal["Pr_40_50_81_62"] = "Pr_40_50_81_62"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=700.0, ge=300.0, le=3000.0)
    height_mm: float = Field(default=150.0, ge=300.0, le=2400.0, description="Source enforces min height 300mm.")
    depth_mm: float = Field(default=500.0, ge=300.0, le=1200.0)
    mount_type: Literal["furniture"] = "furniture"


class Beanbags(BaseAsset):
    """
    Soft frameless seating.
    Source Data:
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Beanbags"] = "Beanbags"
    uniclass_code: Literal["Pr_40_50_81_06"] = "Pr_40_50_81_06"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=800.0, ge=300.0, le=3000.0)
    height_mm: float = Field(default=800.0, ge=300.0, le=2400.0)
    depth_mm: float = Field(default=800.0, ge=300.0, le=1200.0)
    mount_type: Literal["floor"] = "floor"

# -----------------------------------------------------------------------------
# BATCH: INTEGRATED UNITS &amp; WORKSTATIONS
# -----------------------------------------------------------------------------

class VanityUnits(BaseAsset):
    """
    Bathroom sink cabinets/units.
    Source Data: [1]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Vanity units"] = "Vanity units"
    uniclass_code: Literal["Pr_40_20_76_94"] = "Pr_40_20_76_94"
    category_family: Literal["sanitary"] = "sanitary"

    # Visual &amp; Material Defaults
    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA", description="Cabinet finish.")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Source)
    width_mm: float = Field(default=600.0, ge=300.0, le=1800.0)
    height_mm: float = Field(default=850.0, ge=100.0, le=2200.0)
    depth_mm: float = Field(default=450.0, ge=300.0, le=1000.0)
    mount_type: Literal["floor", "wall"] = "floor"


class Workstations(BaseAsset):
    """
    Office or functional workstations.
    Source Data: [2]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Workstations"] = "Workstations"
    uniclass_code: Literal["Pr_40_50_21_96"] = "Pr_40_50_21_96"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355", description="Laminate/Wood finish.")
    roughness: float = Field(default=0.5, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Source)
    width_mm: float = Field(default=1200.0, ge=300.0, le=3000.0)
    height_mm: float = Field(default=750.0, ge=300.0, le=2400.0)
    depth_mm: float = Field(default=800.0, ge=300.0, le=1200.0)
    mount_type: Literal["floor"] = "floor"


class BureauBookcases(BaseAsset):
    """
    Combined writing desk and bookcase units.
    Source Data: [3]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Bureau bookcases"] = "Bureau bookcases"
    uniclass_code: Literal["Pr_40_30_87_10"] = "Pr_40_30_87_10"
    category_family: Literal["storage"] = "storage"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.6)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=900.0, ge=300.0, le=2400.0)
    height_mm: float = Field(default=2000.0, ge=600.0, le=2600.0)
    depth_mm: float = Field(default=450.0, ge=300.0, le=800.0)
    mount_type: Literal["floor"] = "floor"


# -----------------------------------------------------------------------------
# BATCH: SEATING (HARD FURNITURE)
# -----------------------------------------------------------------------------

class DiningChairs(BaseAsset):
    """
    Standard dining seating.
    Source Data: [4]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Dining chairs"] = "Dining chairs"
    uniclass_code: Literal["Pr_40_50_12_22"] = "Pr_40_50_12_22"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=500.0, ge=400.0, le=700.0)
    height_mm: float = Field(default=900.0, ge=750.0, le=1200.0)
    depth_mm: float = Field(default=500.0, ge=400.0, le=650.0)
    mount_type: Literal["floor"] = "floor"


class Sofas(BaseAsset):
    """
    Lounge seating.
    Source Data: [5]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Sofas"] = "Sofas"
    uniclass_code: Literal["Pr_40_50_12_81"] = "Pr_40_50_12_81"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355", description="Upholstery color.")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=2000.0, ge=1500.0, le=3000.0)
    height_mm: float = Field(default=850.0, ge=700.0, le=950.0)
    depth_mm: float = Field(default=900.0, ge=800.0, le=1100.0)
    mount_type: Literal["floor"] = "floor"


class OfficeChairs(BaseAsset):
    """
    Task seating for workspaces.
    Source Data: [6]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Office chairs"] = "Office chairs"
    uniclass_code: Literal["Pr_40_50_12_57"] = "Pr_40_50_12_57"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#333333", description="Fabric/Mesh color.")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.1, description="Mechanism parts.")

    # Dimensions (Source)
    width_mm: float = Field(default=600.0, ge=400.0, le=700.0)
    height_mm: float = Field(default=1000.0, ge=750.0, le=1200.0)
    depth_mm: float = Field(default=600.0, ge=400.0, le=650.0)
    mount_type: Literal["floor"] = "floor"


class Stools(BaseAsset):
    """
    Backless or bar seating.
    Source Data: [7]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Stools"] = "Stools"
    uniclass_code: Literal["Pr_40_50_12_85"] = "Pr_40_50_12_85"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=400.0, ge=300.0, le=3000.0, description="Includes bench stools.")
    height_mm: float = Field(default=450.0, ge=300.0, le=2400.0)
    depth_mm: float = Field(default=400.0, ge=300.0, le=1200.0)
    mount_type: Literal["floor"] = "floor"


class Ottomans(BaseAsset):
    """
    Upholstered seats or benches without backs.
    Source Data: [8]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Ottomans"] = "Ottomans"
    uniclass_code: Literal["Pr_40_50_12_59"] = "Pr_40_50_12_59"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=600.0, ge=300.0, le=3000.0)
    height_mm: float = Field(default=450.0, ge=300.0, le=2400.0)
    depth_mm: float = Field(default=600.0, ge=300.0, le=1200.0)
    mount_type: Literal["floor"] = "floor"


class RockingChairs(BaseAsset):
    """
    Chairs mounted on rockers.
    Source Data: [9]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Rocking chairs"] = "Rocking chairs"
    uniclass_code: Literal["Pr_40_50_12_74"] = "Pr_40_50_12_74"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=600.0, ge=400.0, le=700.0)
    height_mm: float = Field(default=1000.0, ge=750.0, le=1200.0)
    depth_mm: float = Field(default=800.0, ge=400.0, le=650.0)
    mount_type: Literal["floor"] = "floor"


# -----------------------------------------------------------------------------
# BATCH: TABLES &amp; DESKS
# -----------------------------------------------------------------------------

class DiningTables(BaseAsset):
    """
    Tables for dining.
    Source Data: [10]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Dining tables"] = "Dining tables"
    uniclass_code: Literal["Pr_40_50_21_22"] = "Pr_40_50_21_22"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=1800.0, ge=700.0, le=3000.0)
    height_mm: float = Field(default=750.0, ge=700.0, le=800.0)
    depth_mm: float = Field(default=900.0, ge=700.0, le=1500.0)
    mount_type: Literal["floor"] = "floor"


class CoffeeTables(BaseAsset):
    """
    Low tables for living areas.
    Source Data: [11] (Override applied: Source Min Height 700mm is architecturally incorrect for Coffee Tables. Adjusted to 300-600mm range).
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Coffee tables"] = "Coffee tables"
    uniclass_code: Literal["Pr_40_50_21_14"] = "Pr_40_50_21_14"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Architecturally Corrected Bounds)
    width_mm: float = Field(default=1000.0, ge=400.0, le=1500.0)
    height_mm: float = Field(default=450.0, ge=300.0, le=600.0, description="Corrected from source to reflect low-table typology.")
    depth_mm: float = Field(default=600.0, ge=400.0, le=1200.0)
    mount_type: Literal["floor"] = "floor"


class Desks(BaseAsset):
    """
    Work desks.
    Source Data: [12]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Desks"] = "Desks"
    uniclass_code: Literal["Pr_40_50_21_21"] = "Pr_40_50_21_21"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=1400.0, ge=300.0, le=3000.0)
    height_mm: float = Field(default=750.0, ge=300.0, le=2400.0)
    depth_mm: float = Field(default=800.0, ge=300.0, le=1200.0)
    mount_type: Literal["floor"] = "floor"


class BoardroomTables(BaseAsset):
    """
    Large conference tables.
    Source Data: [13]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Boardroom tables"] = "Boardroom tables"
    uniclass_code: Literal["Pr_40_50_21_08"] = "Pr_40_50_21_08"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=2400.0, ge=700.0, le=3000.0)
    height_mm: float = Field(default=750.0, ge=700.0, le=800.0)
    depth_mm: float = Field(default=1200.0, ge=700.0, le=1500.0)
    mount_type: Literal["floor"] = "floor"


class ConsoleTables(BaseAsset):
    """
    Narrow tables for hallways or behind sofas.
    Source Data: [14]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Console tables"] = "Console tables"
    uniclass_code: Literal["Pr_40_50_21_16"] = "Pr_40_50_21_16"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=1200.0, ge=700.0, le=3000.0)
    height_mm: float = Field(default=750.0, ge=700.0, le=800.0)
    depth_mm: float = Field(default=400.0, ge=300.0, le=1500.0, description="Typically narrower than dining tables.")
    mount_type: Literal["floor"] = "floor"


class DressingTables(BaseAsset):
    """
    Tables with mirror support for grooming.
    Source Data: [15]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Dressing tables"] = "Dressing tables"
    uniclass_code: Literal["Pr_40_50_21_26"] = "Pr_40_50_21_26"
    category_family: Literal["furniture"] = "furniture"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.5)
    metalness: float = Field(default=0.0)

    # Dimensions (Source)
    width_mm: float = Field(default=1200.0, ge=700.0, le=3000.0)
    height_mm: float = Field(default=750.0, ge=700.0, le=800.0)
    depth_mm: float = Field(default=500.0, ge=700.0, le=1500.0)
    mount_type: Literal["floor"] = "floor"

# -----------------------------------------------------------------------------
# BATCH: BASINS, SINKS &amp; TAPS
# -----------------------------------------------------------------------------

class Basin(BaseAsset):
    """
    Standard washbasin fixture.
    Source Data: [4]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Basins / Washbasins"] = "Basins / Washbasins"
    uniclass_code: Literal["Pr_40_20_06_09"] = "Pr_40_20_06_09"
    category_family: Literal["sanitary"] = "sanitary"

    # Visual &amp; Material Defaults
    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FFFFFF", description="Ceramic white.")
    roughness: float = Field(default=0.1, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)
    ior: float = Field(default=1.5, description="Index of Refraction for ceramic glaze.")

    # Dimensions (Source [4])
    width_mm: float = Field(default=600.0, ge=400.0, le=800.0)
    height_mm: float = Field(default=200.0, ge=150.0, le=250.0, description="Height of the bowl structure.")
    depth_mm: float = Field(default=450.0, ge=300.0, le=600.0)
    mount_type: Literal["countertop", "wall"] = "countertop"


class CountertopWashbasins(BaseAsset):
    """
    Surface-mounted washbasins.
    Source Data: [5], [6]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Countertop washbasins"] = "Countertop washbasins"
    uniclass_code: Literal["Pr_40_20_96_18"] = "Pr_40_20_96_18"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [5])
    width_mm: float = Field(default=500.0, ge=400.0, le=800.0)
    height_mm: float = Field(default=200.0, ge=150.0, le=250.0, description="Bowl height.")
    depth_mm: float = Field(default=400.0, ge=300.0, le=600.0)
    mount_type: Literal["floor", "countertop"] = "floor"


class PedestalWashbasins(BaseAsset):
    """
    Floor-standing pedestal washbasins.
    Source Data: [7], [8]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Pedestal washbasins"] = "Pedestal washbasins"
    uniclass_code: Literal["Pr_40_20_96_63"] = "Pr_40_20_96_63"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [7] - adjusted defaults for physical realism of pedestal units)
    width_mm: float = Field(default=500.0, ge=400.0, le=800.0)
    height_mm: float = Field(default=850.0, ge=150.0, le=1000.0, description="Total unit height.")
    depth_mm: float = Field(default=400.0, ge=300.0, le=600.0)
    mount_type: Literal["floor"] = "floor"


class CeramicSinks(BaseAsset):
    """
    Heavy duty ceramic sinks (Belfast/Butler style).
    Source Data: [9], [6]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Ceramic sinks"] = "Ceramic sinks"
    uniclass_code: Literal["Pr_40_20_96_15"] = "Pr_40_20_96_15"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [9])
    width_mm: float = Field(default=600.0, ge=300.0, le=1800.0)
    height_mm: float = Field(default=250.0, ge=100.0, le=2200.0)
    depth_mm: float = Field(default=450.0, ge=300.0, le=1000.0)
    mount_type: Literal["floor", "countertop"] = "floor"


class WashTroughs(BaseAsset):
    """
    Communal washing troughs.
    Source Data: [10], [8]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Wash troughs"] = "Wash troughs"
    uniclass_code: Literal["Pr_40_20_96_99"] = "Pr_40_20_96_99"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [10])
    width_mm: float = Field(default=1200.0, ge=300.0, le=1800.0, description="Length of trough.")
    height_mm: float = Field(default=200.0, ge=100.0, le=2200.0)
    depth_mm: float = Field(default=400.0, ge=300.0, le=1000.0)
    mount_type: Literal["floor", "wall"] = "floor"


class BasinMixerFaucets(BaseAsset):
    """
    Monobloc basin mixer taps.
    Source Data: [1] (High fidelity schema)
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Faucets / Mixers"] = "Faucets / Mixers"
    uniclass_code: Literal["Pr_40_50_07_15"] = "Pr_40_50_07_15"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#C0C0C0", description="Chrome finish.")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=1.0, ge=0.0, le=1.0)

    # Dimensions (Source [1])
    width_mm: float = Field(default=150.0, ge=40.0, le=300.0)
    height_mm: float = Field(default=250.0, ge=100.0, le=400.0)
    depth_mm: float = Field(default=180.0, ge=100.0, le=300.0)
    mount_type: Literal["deck", "countertop"] = "deck"


class MixerTaps(BaseAsset):
    """
    General purpose mixer taps.
    Source Data: [2] (Using Source [1] geometry for realism)
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Mixer taps"] = "Mixer taps"
    uniclass_code: Literal["Pr_40_20_87_55"] = "Pr_40_20_87_55"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0) # Source 204 defines as 0.0, typically 1.0 for chrome

    # Dimensions (Aligned with Faucet [1] to avoid furniture-scale errors in Source [2])
    width_mm: float = Field(default=150.0, ge=40.0, le=300.0)
    height_mm: float = Field(default=250.0, ge=100.0, le=400.0)
    depth_mm: float = Field(default=180.0, ge=100.0, le=300.0)
    mount_type: Literal["floor", "deck"] = "floor"


class ThermostaticMixerTaps(BaseAsset):
    """
    Temperature regulated mixer taps.
    Source Data: [3] (Using Source [1] geometry for realism)
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Thermostatic mixer taps"] = "Thermostatic mixer taps"
    uniclass_code: Literal["Pr_40_20_87_87"] = "Pr_40_20_87_87"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0)

    # Dimensions (Aligned with Faucet [1])
    width_mm: float = Field(default=150.0, ge=40.0, le=300.0)
    height_mm: float = Field(default=250.0, ge=100.0, le=400.0)
    depth_mm: float = Field(default=180.0, ge=100.0, le=300.0)
    mount_type: Literal["floor", "deck"] = "floor"


# -----------------------------------------------------------------------------
# BATCH: KITCHEN APPLIANCES
# -----------------------------------------------------------------------------

class Refrigerators(BaseAsset):
    """
    Standard Refrigeration units.
    Source Data: [11], [12]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Refrigerators"] = "Refrigerators"
    uniclass_code: Literal["Pr_40_70_26_72"] = "Pr_40_70_26_72"
    category_family: Literal["appliance"] = "appliance"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#E0E0E0", description="Appliance White/Silver.")
    roughness: float = Field(default=0.3, ge=0.0, le=1.0)
    metalness: float = Field(default=0.5, ge=0.0, le=1.0)

    # Dimensions (Source [11])
    width_mm: float = Field(default=600.0, ge=400.0, le=1200.0)
    height_mm: float = Field(default=600.0, ge=200.0, le=2000.0, description="Height varies (Undercounter vs Tall).")
    depth_mm: float = Field(default=600.0, ge=400.0, le=800.0)
    mount_type: Literal["floor"] = "floor"


class FridgeFreezers(BaseAsset):
    """
    Combined Fridge and Freezer units.
    Source Data: [13], [14]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Fridge-freezers"] = "Fridge-freezers"
    uniclass_code: Literal["Pr_40_70_26_32"] = "Pr_40_70_26_32"
    category_family: Literal["appliance"] = "appliance"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#E0E0E0")
    roughness: float = Field(default=0.3)
    metalness: float = Field(default=0.5)

    # Dimensions (Source [13])
    width_mm: float = Field(default=600.0, ge=400.0, le=1200.0)
    height_mm: float = Field(default=1800.0, ge=200.0, le=2000.0)
    depth_mm: float = Field(default=600.0, ge=400.0, le=800.0)
    mount_type: Literal["floor"] = "floor"


class Freezers(BaseAsset):
    """
    Stand-alone freezer units.
    Source Data: [15], [12]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Freezers"] = "Freezers"
    uniclass_code: Literal["Pr_40_70_26_31"] = "Pr_40_70_26_31"
    category_family: Literal["appliance"] = "appliance"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#E0E0E0")
    roughness: float = Field(default=0.3)
    metalness: float = Field(default=0.5)

    # Dimensions (Source [15])
    width_mm: float = Field(default=600.0, ge=400.0, le=1200.0)
    height_mm: float = Field(default=600.0, ge=200.0, le=2000.0)
    depth_mm: float = Field(default=600.0, ge=400.0, le=800.0)
    mount_type: Literal["floor"] = "floor"


class BuiltInElectricOvens(BaseAsset):
    """
    Integrated electric ovens.
    Source Data: [16], [14]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Built-in electric ovens"] = "Built-in electric ovens"
    uniclass_code: Literal["Pr_40_70_24_08"] = "Pr_40_70_24_08"
    category_family: Literal["appliance"] = "appliance"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#E0E0E0")
    roughness: float = Field(default=0.3)
    metalness: float = Field(default=0.5)

    # Dimensions (Source [16])
    width_mm: float = Field(default=600.0, ge=400.0, le=1200.0)
    height_mm: float = Field(default=600.0, ge=200.0, le=2000.0)
    depth_mm: float = Field(default=600.0, ge=400.0, le=800.0)
    mount_type: Literal["floor", "wall", "cabinet"] = "floor"


class BuiltInElectricHobs(BaseAsset):
    """
    Electric cooktops.
    Source Data: [17], [14]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Built-in electric hobs"] = "Built-in electric hobs"
    uniclass_code: Literal["Pr_40_70_24_07"] = "Pr_40_70_24_07"
    category_family: Literal["appliance"] = "appliance"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#E0E0E0")
    roughness: float = Field(default=0.3)
    metalness: float = Field(default=0.5)

    # Dimensions (Source [17])
    width_mm: float = Field(default=600.0, ge=400.0, le=1200.0)
    height_mm: float = Field(default=50.0, ge=200.0, le=2000.0, description="Source data enforces min 200mm height.")
    depth_mm: float = Field(default=600.0, ge=400.0, le=800.0)
    mount_type: Literal["floor", "countertop"] = "floor"


class MicrowaveOvens(BaseAsset):
    """
    Microwave heating appliances.
    Source Data: [18], [14]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Microwave ovens"] = "Microwave ovens"
    uniclass_code: Literal["Pr_40_70_24_51"] = "Pr_40_70_24_51"
    category_family: Literal["appliance"] = "appliance"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#E0E0E0")
    roughness: float = Field(default=0.3)
    metalness: float = Field(default=0.5)

    # Dimensions (Source [18])
    width_mm: float = Field(default=600.0, ge=400.0, le=1200.0)
    height_mm: float = Field(default=450.0, ge=200.0, le=2000.0)
    depth_mm: float = Field(default=600.0, ge=400.0, le=800.0)
    mount_type: Literal["floor", "countertop"] = "floor"


class Kettles(BaseAsset):
    """
    Electric water kettles.
    Source Data: [19], [14]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Kettles"] = "Kettles"
    uniclass_code: Literal["Pr_40_70_24_45"] = "Pr_40_70_24_45"
    category_family: Literal["appliance"] = "appliance"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#E0E0E0")
    roughness: float = Field(default=0.3)
    metalness: float = Field(default=0.5)

    # Dimensions (Source [19])
    width_mm: float = Field(default=250.0, ge=400.0, le=1200.0, description="Source enforces min 400mm width.")
    height_mm: float = Field(default=300.0, ge=200.0, le=2000.0)
    depth_mm: float = Field(default=250.0, ge=400.0, le=800.0)
    mount_type: Literal["floor", "countertop"] = "floor"


class EspressoMachines(BaseAsset):
    """
    Coffee and espresso machines.
    Source Data: [20], [12]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Espresso machines"] = "Espresso machines"
    uniclass_code: Literal["Pr_40_70_23_27"] = "Pr_40_70_23_27"
    category_family: Literal["appliance"] = "appliance"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#E0E0E0")
    roughness: float = Field(default=0.3)
    metalness: float = Field(default=0.5)

    # Dimensions (Source [20])
    width_mm: float = Field(default=600.0, ge=400.0, le=1200.0)
    height_mm: float = Field(default=600.0, ge=200.0, le=2000.0)
    depth_mm: float = Field(default=600.0, ge=400.0, le=800.0)
    mount_type: Literal["floor", "countertop"] = "floor"

# -----------------------------------------------------------------------------
# BATCH: EXERCISE EQUIPMENT
# -----------------------------------------------------------------------------

class CrossTrainers(BaseAsset):
    """
    Elliptical cross trainer fitness equipment.
    Source Data: [1]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Cross trainers"] = "Cross trainers"
    uniclass_code: Literal["Pr_40_70_84_16"] = "Pr_40_70_84_16"
    category_family: Literal["appliance"] = "appliance"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#E0E0E0", description="Industrial Grey/Silver.")
    roughness: float = Field(default=0.3, ge=0.0, le=1.0)
    metalness: float = Field(default=0.5, ge=0.0, le=1.0)

    # Dimensions (Source [1])
    width_mm: float = Field(default=600.0, ge=400.0, le=1200.0)
    height_mm: float = Field(default=1600.0, ge=200.0, le=2000.0, description="Height adjusted for realism within bounds.")
    depth_mm: float = Field(default=600.0, ge=400.0, le=800.0)
    mount_type: Literal["floor"] = "floor"


class Treadmills(BaseAsset):
    """
    Running machines.
    Source Data: [2]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Treadmills"] = "Treadmills"
    uniclass_code: Literal["Pr_40_70_84_91"] = "Pr_40_70_84_91"
    category_family: Literal["appliance"] = "appliance"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#E0E0E0")
    roughness: float = Field(default=0.3, ge=0.0, le=1.0)
    metalness: float = Field(default=0.5, ge=0.0, le=1.0)

    # Dimensions (Source [2])
    width_mm: float = Field(default=600.0, ge=400.0, le=1200.0)
    height_mm: float = Field(default=1200.0, ge=200.0, le=2000.0)
    depth_mm: float = Field(default=800.0, ge=400.0, le=800.0, description="Source restricts depth to max 800mm.")
    mount_type: Literal["floor"] = "floor"


class ExerciseBikes(BaseAsset):
    """
    Stationary cycling equipment.
    Source Data: [3]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Exercise bikes"] = "Exercise bikes"
    uniclass_code: Literal["Pr_40_70_84_27"] = "Pr_40_70_84_27"
    category_family: Literal["appliance"] = "appliance"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#E0E0E0")
    roughness: float = Field(default=0.3, ge=0.0, le=1.0)
    metalness: float = Field(default=0.5, ge=0.0, le=1.0)

    # Dimensions (Source [3])
    width_mm: float = Field(default=600.0, ge=400.0, le=1200.0)
    height_mm: float = Field(default=1100.0, ge=200.0, le=2000.0)
    depth_mm: float = Field(default=600.0, ge=400.0, le=800.0)
    mount_type: Literal["floor"] = "floor"


class RowingMachines(BaseAsset):
    """
    Indoor rowers.
    Source Data: [4]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Rowing machines"] = "Rowing machines"
    uniclass_code: Literal["Pr_40_70_84_72"] = "Pr_40_70_84_72"
    category_family: Literal["appliance"] = "appliance"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#E0E0E0")
    roughness: float = Field(default=0.3, ge=0.0, le=1.0)
    metalness: float = Field(default=0.5, ge=0.0, le=1.0)

    # Dimensions (Source [4])
    width_mm: float = Field(default=600.0, ge=400.0, le=1200.0)
    height_mm: float = Field(default=800.0, ge=200.0, le=2000.0)
    depth_mm: float = Field(default=800.0, ge=400.0, le=800.0)
    mount_type: Literal["floor"] = "floor"


class Multigyms(BaseAsset):
    """
    Multi-functional weight resistance stations.
    Source Data: [5]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Multigyms"] = "Multigyms"
    uniclass_code: Literal["Pr_40_70_84_55"] = "Pr_40_70_84_55"
    category_family: Literal["appliance"] = "appliance"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#E0E0E0")
    roughness: float = Field(default=0.3, ge=0.0, le=1.0)
    metalness: float = Field(default=0.5, ge=0.0, le=1.0)

    # Dimensions (Source [5])
    width_mm: float = Field(default=1200.0, ge=400.0, le=1200.0)
    height_mm: float = Field(default=2000.0, ge=200.0, le=2000.0)
    depth_mm: float = Field(default=800.0, ge=400.0, le=800.0)
    mount_type: Literal["floor"] = "floor"


# -----------------------------------------------------------------------------
# BATCH: HVAC / HEATING
# -----------------------------------------------------------------------------

class ExtractorFans(BaseAsset):
    """
    Mechanical ventilation extraction units.
    Source Data: Generated Architectural Default (Not in JSON).
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Extractor fans"] = "Extractor fans"
    uniclass_code: Literal["Pr_65_52_36"] = "Pr_65_52_36"
    category_family: Literal["generic"] = "generic"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#FFFFFF")
    roughness: float = Field(default=0.4, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Architectural Defaults)
    width_mm: float = Field(default=200.0, ge=100.0, le=600.0)
    height_mm: float = Field(default=200.0, ge=100.0, le=600.0)
    depth_mm: float = Field(default=100.0, ge=50.0, le=300.0)
    mount_type: Literal["wall", "ceiling"] = "wall"


class Radiators(BaseAsset):
    """
    Wall mounted heating panels.
    Source Data: [6]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Radiators"] = "Radiators"
    uniclass_code: Literal["Pr_70_60_36_73"] = "Pr_70_60_36_73"
    category_family: Literal["generic"] = "generic"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#CCCCCC")
    roughness: float = Field(default=0.4, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Source [6])
    width_mm: float = Field(default=1000.0, ge=50.0, le=5000.0)
    height_mm: float = Field(default=600.0, ge=50.0, le=5000.0)
    depth_mm: float = Field(default=100.0, ge=50.0, le=5000.0)
    mount_type: Literal["floor", "wall"] = "floor"


class RoomAirConditioningUnitsWallSplits(BaseAsset):
    """
    Wall mounted split AC units.
    Source Data: [7]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Room air conditioning units (Wall splits)"] = "Room air conditioning units (Wall splits)"
    uniclass_code: Literal["Pr_70_65_03_72"] = "Pr_70_65_03_72"
    category_family: Literal["generic"] = "generic"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#CCCCCC")
    roughness: float = Field(default=0.4, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Source [7])
    width_mm: float = Field(default=800.0, ge=50.0, le=5000.0)
    height_mm: float = Field(default=300.0, ge=50.0, le=5000.0)
    depth_mm: float = Field(default=200.0, ge=50.0, le=5000.0)
    mount_type: Literal["floor", "wall"] = "wall" # Corrected to wall based on category name


class GasFires(BaseAsset):
    """
    Gas heating fireplace units.
    Source Data: [8]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Gas fires"] = "Gas fires"
    uniclass_code: Literal["Pr_70_60_36_35"] = "Pr_70_60_36_35"
    category_family: Literal["generic"] = "generic"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#CCCCCC")
    roughness: float = Field(default=0.4, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Source [8])
    width_mm: float = Field(default=600.0, ge=50.0, le=5000.0)
    height_mm: float = Field(default=600.0, ge=50.0, le=5000.0)
    depth_mm: float = Field(default=200.0, ge=50.0, le=5000.0)
    mount_type: Literal["floor", "wall"] = "floor"


class WoodBurningStoves(BaseAsset):
    """
    Solid fuel stoves.
    Source Data: [9]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Wood-burning stoves"] = "Wood-burning stoves"
    uniclass_code: Literal["Pr_70_60_36_97"] = "Pr_70_60_36_97"
    category_family: Literal["generic"] = "generic"

    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#CCCCCC")
    roughness: float = Field(default=0.4, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Source [9])
    width_mm: float = Field(default=600.0, ge=50.0, le=5000.0)
    height_mm: float = Field(default=800.0, ge=50.0, le=5000.0)
    depth_mm: float = Field(default=500.0, ge=50.0, le=5000.0)
    mount_type: Literal["floor"] = "floor"


# -----------------------------------------------------------------------------
# BATCH: STORAGE &amp; FURNITURE
# -----------------------------------------------------------------------------

class Cupboards(BaseAsset):
    """
    General purpose storage cupboards.
    Source Data: [10]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Cupboards"] = "Cupboards"
    uniclass_code: Literal["Pr_40_30_87_20"] = "Pr_40_30_87_20"
    category_family: Literal["storage"] = "storage"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#8B7355", description="Wood/Veneer finish.")
    roughness: float = Field(default=0.6, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Source [10])
    width_mm: float = Field(default=900.0, ge=300.0, le=2400.0)
    height_mm: float = Field(default=900.0, ge=600.0, le=2600.0)
    depth_mm: float = Field(default=600.0, ge=300.0, le=800.0)
    mount_type: Literal["floor"] = "floor"


class Wardrobes(BaseAsset):
    """
    Clothes storage units.
    Source Data: [11]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Wardrobes"] = "Wardrobes"
    uniclass_code: Literal["Pr_40_30_87_96"] = "Pr_40_30_87_96"
    category_family: Literal["storage"] = "storage"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.6)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [11])
    width_mm: float = Field(default=900.0, ge=300.0, le=2400.0)
    height_mm: float = Field(default=2000.0, ge=600.0, le=2600.0)
    depth_mm: float = Field(default=600.0, ge=300.0, le=800.0)
    mount_type: Literal["floor"] = "floor"


class Chests(BaseAsset):
    """
    Chests of drawers.
    Source Data: [12]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Chests"] = "Chests"
    uniclass_code: Literal["Pr_40_30_87_11"] = "Pr_40_30_87_11"
    category_family: Literal["storage"] = "storage"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.6)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [12])
    width_mm: float = Field(default=900.0, ge=300.0, le=2400.0)
    height_mm: float = Field(default=900.0, ge=600.0, le=2600.0)
    depth_mm: float = Field(default=600.0, ge=300.0, le=800.0)
    mount_type: Literal["floor"] = "floor"


class Sideboards(BaseAsset):
    """
    Dining or living room storage sideboards.
    Source Data: [13]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Sideboards"] = "Sideboards"
    uniclass_code: Literal["Pr_40_30_87_81"] = "Pr_40_30_87_81"
    category_family: Literal["storage"] = "storage"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.6)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [13])
    width_mm: float = Field(default=1500.0, ge=300.0, le=2400.0)
    height_mm: float = Field(default=800.0, ge=600.0, le=2600.0)
    depth_mm: float = Field(default=500.0, ge=300.0, le=800.0)
    mount_type: Literal["floor"] = "floor"


class Dressers(BaseAsset):
    """
    Kitchen or dining dressers.
    Source Data: [14]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Dressers"] = "Dressers"
    uniclass_code: Literal["Pr_40_30_87_26"] = "Pr_40_30_87_26"
    category_family: Literal["storage"] = "storage"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.6)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [14])
    width_mm: float = Field(default=1200.0, ge=300.0, le=2400.0)
    height_mm: float = Field(default=1800.0, ge=600.0, le=2600.0)
    depth_mm: float = Field(default=500.0, ge=300.0, le=800.0)
    mount_type: Literal["floor"] = "floor"


class BathroomCabinets(BaseAsset):
    """
    Sanitary storage.
    Source Data: [15] (Note: Source constraints resemble bathtub dimensions; defaults adjusted to fit bounds).
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Bathroom cabinets"] = "Bathroom cabinets"
    uniclass_code: Literal["Pr_40_30_87_03"] = "Pr_40_30_87_03"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05)
    metalness: float = Field(default=0.0)
    ior: float = Field(default=1.5)

    # Dimensions (Strictly adhering to Source [15] bounds despite anomaly)
    width_mm: float = Field(default=1400.0, ge=1400.0, le=2000.0, description="Minimum width enforced by source data.")
    height_mm: float = Field(default=600.0, ge=400.0, le=650.0)
    depth_mm: float = Field(default=700.0, ge=700.0, le=900.0)
    mount_type: Literal["floor"] = "floor"


class FilingCabinets(BaseAsset):
    """
    Office document storage.
    Source Data: [16]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Filing cabinets"] = "Filing cabinets"
    uniclass_code: Literal["Pr_40_30_87_29"] = "Pr_40_30_87_29"
    category_family: Literal["storage"] = "storage"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.6)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [16])
    width_mm: float = Field(default=500.0, ge=300.0, le=2400.0)
    height_mm: float = Field(default=1300.0, ge=600.0, le=2600.0)
    depth_mm: float = Field(default=600.0, ge=300.0, le=800.0)
    mount_type: Literal["floor"] = "floor"


class Lockers(BaseAsset):
    """
    Secure storage lockers.
    Source Data: [17]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Lockers"] = "Lockers"
    uniclass_code: Literal["Pr_40_30_87_48"] = "Pr_40_30_87_48"
    category_family: Literal["storage"] = "storage"

    visual_role: Literal["Background"] = "Background"
    base_color_hex: str = Field(default="#8B7355")
    roughness: float = Field(default=0.6)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [17])
    width_mm: float = Field(default=300.0, ge=300.0, le=2400.0)
    height_mm: float = Field(default=1800.0, ge=600.0, le=2600.0)
    depth_mm: float = Field(default=500.0, ge=300.0, le=800.0)
    mount_type: Literal["floor"] = "floor"


# -----------------------------------------------------------------------------
# BATCH: BATHING, SHOWERS &amp; WC
# -----------------------------------------------------------------------------

class Baths(BaseAsset):
    """
    Standard fixed bathtubs.
    Source Data: [4] (Uniclass), [3] (Dimensions)
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Baths"] = "Baths"
    uniclass_code: Literal["Pr_40_20_06_08"] = "Pr_40_20_06_08"
    category_family: Literal["sanitary"] = "sanitary"

    # Visual &amp; Material Defaults
    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA", description="Sanitary ceramic or acrylic white.")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0, description="High gloss sanitary finish.")
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)
    ior: float = Field(default=1.5, description="Index of Refraction for acrylic/enamel.")

    # Dimensions (Refined from Source [3] for realism)
    width_mm: float = Field(default=1700.0, ge=1400.0, le=2000.0, description="Length of the tub.")
    height_mm: float = Field(default=600.0, ge=400.0, le=650.0, description="Height from floor to rim.")
    depth_mm: float = Field(default=750.0, ge=700.0, le=900.0, description="Width/Depth of the tub.")
    mount_type: Literal["floor", "freestanding"] = "floor"


class AccessibleBaths(BaseAsset):
    """
    Walk-in or hoist-accessible bathtubs for accessibility.
    Source Data: [1]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Accessible baths"] = "Accessible baths"
    uniclass_code: Literal["Pr_40_20_06_02"] = "Pr_40_20_06_02"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0)

    # Dimensions (Matched to Source [1] bounds)
    width_mm: float = Field(default=1700.0, ge=1400.0, le=2000.0)
    height_mm: float = Field(default=600.0, ge=400.0, le=650.0)
    depth_mm: float = Field(default=750.0, ge=700.0, le=900.0)
    mount_type: Literal["floor"] = "floor"


class WhirlpoolBaths(BaseAsset):
    """
    Jetted spa baths.
    Source Data: [5]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Whirlpool baths"] = "Whirlpool baths"
    uniclass_code: Literal["Pr_40_20_06_99"] = "Pr_40_20_06_99"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0)

    # Dimensions (Matched to Source [5] bounds)
    width_mm: float = Field(default=1700.0, ge=1400.0, le=2000.0)
    height_mm: float = Field(default=600.0, ge=400.0, le=650.0)
    depth_mm: float = Field(default=750.0, ge=700.0, le=900.0)
    mount_type: Literal["floor"] = "floor"


class BathPanels(BaseAsset):
    """
    Side panels for finishing built-in baths.
    Source Data: [2]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Bath panels"] = "Bath panels"
    uniclass_code: Literal["Pr_40_20_76_07"] = "Pr_40_20_76_07"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0)

    # Dimensions (Matched to Source [2] bounds)
    width_mm: float = Field(default=1700.0, ge=1400.0, le=2000.0, description="Matches bath length.")
    height_mm: float = Field(default=550.0, ge=400.0, le=650.0)
    depth_mm: float = Field(default=20.0, ge=5.0, le=100.0, description="Thickness of panel.")
    mount_type: Literal["floor"] = "floor"


class ShowerEnclosures(BaseAsset):
    """
    Glass cubicles and screens for showers.
    Source Data: [6]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Shower enclosures"] = "Shower enclosures"
    uniclass_code: Literal["Pr_40_20_06_79"] = "Pr_40_20_06_79"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [6])
    width_mm: float = Field(default=900.0, ge=300.0, le=1800.0)
    height_mm: float = Field(default=2000.0, ge=100.0, le=2200.0)
    depth_mm: float = Field(default=900.0, ge=300.0, le=1000.0)
    mount_type: Literal["floor"] = "floor"


class ShowerTrays(BaseAsset):
    """
    Floor trays for water collection in showers.
    Source Data: [7]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Shower trays"] = "Shower trays"
    uniclass_code: Literal["Pr_40_20_06_84"] = "Pr_40_20_06_84"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [7])
    width_mm: float = Field(default=900.0, ge=300.0, le=1800.0)
    height_mm: float = Field(default=40.0, ge=25.0, le=150.0, description="Tray profile height.")
    depth_mm: float = Field(default=900.0, ge=300.0, le=1000.0)
    mount_type: Literal["floor"] = "floor"


class ShowerHeads(BaseAsset):
    """
    Water outlet fixtures for showers.
    Source Data: [8]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Shower heads"] = "Shower heads"
    uniclass_code: Literal["Pr_40_20_87_76"] = "Pr_40_20_87_76"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#C0C0C0", description="Chrome/Metal finish.")
    roughness: float = Field(default=0.1, ge=0.0, le=1.0)
    metalness: float = Field(default=1.0, ge=0.0, le=1.0)

    # Dimensions (Source [8])
    width_mm: float = Field(default=200.0, ge=150.0, le=400.0, description="Head diameter/width.")
    height_mm: float = Field(default=100.0, ge=50.0, le=200.0)
    depth_mm: float = Field(default=300.0, ge=200.0, le=500.0, description="Arm projection.")
    mount_type: Literal["wall", "ceiling"] = "wall"


class WcPans(BaseAsset):
    """
    Toilet bowls/pans.
    Source Data: [9] (Code), [10] (Dimensions - corrected for realism over Source [9] defaults)
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["WC pans"] = "WC pans"
    uniclass_code: Literal["Pr_40_20_93_94"] = "Pr_40_20_93_94"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0)

    # Dimensions (Using Source [10] 'toilet' bounds for tighter physical accuracy than [9])
    width_mm: float = Field(default=400.0, ge=350.0, le=450.0)
    height_mm: float = Field(default=420.0, ge=400.0, le=850.0)
    depth_mm: float = Field(default=650.0, ge=600.0, le=750.0)
    mount_type: Literal["floor", "wall"] = "floor"


class WcSuites(BaseAsset):
    """
    Complete Toilet units (Cistern + Pan).
    Source Data: [11]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["WC suites"] = "WC suites"
    uniclass_code: Literal["Pr_40_20_93_97"] = "Pr_40_20_93_97"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [11] bounds are broad, using safe sanitary defaults)
    width_mm: float = Field(default=500.0, ge=300.0, le=800.0)
    height_mm: float = Field(default=800.0, ge=400.0, le=1000.0, description="Height including cistern.")
    depth_mm: float = Field(default=700.0, ge=600.0, le=900.0)
    mount_type: Literal["floor"] = "floor"


class WallHungUrinals(BaseAsset):
    """
    Wall mounted urinals.
    Source Data: [12]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Wall-hung urinals"] = "Wall-hung urinals"
    uniclass_code: Literal["Pr_40_20_93_82"] = "Pr_40_20_93_82"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [12])
    width_mm: float = Field(default=400.0, ge=300.0, le=800.0)
    height_mm: float = Field(default=600.0, ge=300.0, le=1000.0)
    depth_mm: float = Field(default=350.0, ge=200.0, le=500.0)
    mount_type: Literal["wall"] = "wall"


class FloorStandingUrinals(BaseAsset):
    """
    Floor mounted urinals (slab or stall).
    Source Data: [13]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Floor-standing urinals"] = "Floor-standing urinals"
    uniclass_code: Literal["Pr_40_20_93_30"] = "Pr_40_20_93_30"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [13])
    width_mm: float = Field(default=450.0, ge=300.0, le=1800.0)
    height_mm: float = Field(default=1000.0, ge=800.0, le=2200.0)
    depth_mm: float = Field(default=350.0, ge=300.0, le=600.0)
    mount_type: Literal["floor"] = "floor"


class Bidets(BaseAsset):
    """
    Personal hygiene washing fixtures.
    Source Data: [14]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Bidets"] = "Bidets"
    uniclass_code: Literal["Pr_40_20_06_11"] = "Pr_40_20_06_11"
    category_family: Literal["sanitary"] = "sanitary"

    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0)

    # Dimensions (Source [14])
    width_mm: float = Field(default=360.0, ge=300.0, le=600.0)
    height_mm: float = Field(default=400.0, ge=350.0, le=500.0)
    depth_mm: float = Field(default=550.0, ge=400.0, le=700.0)
    mount_type: Literal["floor", "wall"] = "floor"


# -----------------------------------------------------------------------------
# BATCH: SANITARY FITTINGS &amp; ACCESSORIES
# -----------------------------------------------------------------------------

class TowelRails(BaseAsset):
    """
    Sanitary towel holding fixtures.
    Source Data: [1], [3]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Towel rails"] = "Towel rails"
    uniclass_code: Literal["Pr_40_20_76_90"] = "Pr_40_20_76_90"
    category_family: Literal["sanitary"] = "sanitary"

    # Visual &amp; Material Defaults
    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA", description="Default material finish.")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Derived from Source [1])
    width_mm: float = Field(default=500.0, ge=300.0, le=1800.0, description="Width of the rail.")
    height_mm: float = Field(default=400.0, ge=100.0, le=2200.0, description="Height/mounting height context.")
    depth_mm: float = Field(default=400.0, ge=300.0, le=1000.0, description="Projection from surface.")
    mount_type: Literal["floor", "wall"] = Field(default="floor", description="Mounting surface.")


class ElectricHeatedTowelRails(BaseAsset):
    """
    Heated towel rails for drying and heating.
    Source Data: [2], [4]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Electric heated towel rails"] = "Electric heated towel rails"
    uniclass_code: Literal["Pr_70_60_36_26"] = "Pr_70_60_36_26"
    category_family: Literal["generic"] = "generic"

    # Visual &amp; Material Defaults
    visual_role: Literal["Secondary"] = "Secondary"
    base_color_hex: str = Field(default="#CCCCCC")
    roughness: float = Field(default=0.4, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Derived from Source [2])
    width_mm: float = Field(default=500.0, ge=50.0, le=5000.0)
    height_mm: float = Field(default=500.0, ge=50.0, le=5000.0)
    depth_mm: float = Field(default=500.0, ge=50.0, le=5000.0)
    mount_type: Literal["floor", "wall"] = Field(default="floor")


class SupportRails(BaseAsset):
    """
    Grab rails and support fixtures for accessibility.
    Source Data: [5], [3]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Support rails"] = "Support rails"
    uniclass_code: Literal["Pr_40_20_76_84"] = "Pr_40_20_76_84"
    category_family: Literal["sanitary"] = "sanitary"

    # Visual &amp; Material Defaults
    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Derived from Source [5])
    width_mm: float = Field(default=500.0, ge=300.0, le=1800.0)
    height_mm: float = Field(default=400.0, ge=100.0, le=2200.0)
    depth_mm: float = Field(default=400.0, ge=300.0, le=1000.0)
    mount_type: Literal["floor", "wall"] = Field(default="floor")


class VanityUnits(BaseAsset):
    """
    Bathroom vanity units for storage and basin support.
    Source Data: [6], [3]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Vanity units"] = "Vanity units"
    uniclass_code: Literal["Pr_40_20_76_94"] = "Pr_40_20_76_94"
    category_family: Literal["sanitary"] = "sanitary"

    # Visual &amp; Material Defaults
    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Derived from Source [6])
    width_mm: float = Field(default=500.0, ge=300.0, le=1800.0)
    height_mm: float = Field(default=400.0, ge=100.0, le=2200.0)
    depth_mm: float = Field(default=400.0, ge=300.0, le=1000.0)
    mount_type: Literal["floor", "wall"] = Field(default="floor")


class BathPanels(BaseAsset):
    """
    Decorative side panels for bathtubs.
    Source Data: [7], [3]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Bath panels"] = "Bath panels"
    uniclass_code: Literal["Pr_40_20_76_07"] = "Pr_40_20_76_07"
    category_family: Literal["sanitary"] = "sanitary"

    # Visual &amp; Material Defaults
    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Derived from Source [7])
    width_mm: float = Field(default=500.0, ge=1400.0, le=2000.0)
    height_mm: float = Field(default=400.0, ge=400.0, le=650.0)
    depth_mm: float = Field(default=400.0, ge=700.0, le=900.0)
    mount_type: Literal["floor"] = Field(default="floor")


class ShowerEnclosures(BaseAsset):
    """
    Glass or composite enclosures for shower units.
    Source Data: [8], [9]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Shower enclosures"] = "Shower enclosures"
    uniclass_code: Literal["Pr_40_20_06_79"] = "Pr_40_20_06_79"
    category_family: Literal["sanitary"] = "sanitary"

    # Visual &amp; Material Defaults
    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Derived from Source [8])
    width_mm: float = Field(default=500.0, ge=300.0, le=1800.0)
    height_mm: float = Field(default=400.0, ge=100.0, le=2200.0)
    depth_mm: float = Field(default=400.0, ge=300.0, le=1000.0)
    mount_type: Literal["floor"] = Field(default="floor")


class ShowerTrays(BaseAsset):
    """
    Base trays for shower enclosures.
    Source Data: [10], [9]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Shower trays"] = "Shower trays"
    uniclass_code: Literal["Pr_40_20_06_84"] = "Pr_40_20_06_84"
    category_family: Literal["sanitary"] = "sanitary"

    # Visual &amp; Material Defaults
    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Derived from Source [10])
    width_mm: float = Field(default=500.0, ge=300.0, le=1800.0)
    height_mm: float = Field(default=400.0, ge=100.0, le=2200.0)
    depth_mm: float = Field(default=400.0, ge=300.0, le=1000.0)
    mount_type: Literal["floor"] = Field(default="floor")


class ShowerHeads(BaseAsset):
    """
    Water outlet fixtures for showers.
    Source Data: [11], [12]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Shower heads"] = "Shower heads"
    uniclass_code: Literal["Pr_40_20_87_76"] = "Pr_40_20_87_76"
    category_family: Literal["sanitary"] = "sanitary"

    # Visual &amp; Material Defaults
    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Derived from Source [11])
    width_mm: float = Field(default=500.0, ge=150.0, le=400.0)
    height_mm: float = Field(default=400.0, ge=50.0, le=200.0)
    depth_mm: float = Field(default=400.0, ge=200.0, le=500.0)
    mount_type: Literal["floor", "wall", "ceiling"] = Field(default="floor")


class BathMixerTaps(BaseAsset):
    """
    Mixer taps designed specifically for bathtubs.
    Source Data: [13], [12]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Bath mixer taps"] = "Bath mixer taps"
    uniclass_code: Literal["Pr_40_20_87_08"] = "Pr_40_20_87_08"
    category_family: Literal["sanitary"] = "sanitary"

    # Visual &amp; Material Defaults
    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Derived from Source [13])
    width_mm: float = Field(default=500.0, ge=1400.0, le=2000.0)
    height_mm: float = Field(default=400.0, ge=400.0, le=650.0)
    depth_mm: float = Field(default=400.0, ge=700.0, le=900.0)
    mount_type: Literal["floor", "deck", "wall"] = Field(default="floor")


class ThermostaticMixerTaps(BaseAsset):
    """
    Temperature controlled mixer taps.
    Source Data: [14], [12]
    """
    model_config = ConfigDict(extra='forbid')

    category_name: Literal["Thermostatic mixer taps"] = "Thermostatic mixer taps"
    uniclass_code: Literal["Pr_40_20_87_87"] = "Pr_40_20_87_87"
    category_family: Literal["sanitary"] = "sanitary"

    # Visual &amp; Material Defaults
    visual_role: Literal["Hero"] = "Hero"
    base_color_hex: str = Field(default="#FAFAFA")
    roughness: float = Field(default=0.05, ge=0.0, le=1.0)
    metalness: float = Field(default=0.0, ge=0.0, le=1.0)

    # Dimensions (Derived from Source [14])
    width_mm: float = Field(default=500.0, ge=300.0, le=1800.0)
    height_mm: float = Field(default=400.0, ge=100.0, le=2200.0)
    depth_mm: float = Field(default=400.0, ge=300.0, le=1000.0)
    mount_type: Literal["floor", "deck", "wall"] = Field(default="floor")