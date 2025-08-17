# 16962117 - Gnarled Root

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Tahrongi (ID: 45) |
| Block Size       | 72 bytes                    |
| Total Events     | 2                           |
| References Count | 4                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [328](#event-328)     | 0x0001       |     28 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1EE9      |        7913 |
|       1 | 0x1EEA      |        7914 |
|       2 | 0x0078      |         120 |
|       3 | 0x1EEB      |        7915 |

## String References

- **7913**: This would seem a suitable place to apply Piketo-Puketo's $3.
- **7914**: <Player> injected the $3 into the %.
- **7915**: You hear the thud of an object striking the ground beside you.

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 328

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 28 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 4A F0 FF FF 7F F8  FF FF 7F 6F 70 48 00 80   BJ........opH..
0010: 23 48 01 80 1C 02 80 48  03 80 23 21 00           #H.....H..#!.   
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x4A] LocalPlayer looks at EventEntity
  2: 0x000B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x000C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x000D [0x48] [System] [7913*]:
    → "This would seem a suitable place to apply Piketo-Puketo's $3."
  5: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0011 [0x48] [System] [7914*]:
    → "<Player> injected the $3 into the %."
  7: 0x0014 [0x1C] WAIT(120* ticks)
  8: 0x0017 [0x48] [System] [7915*]:
    → "You hear the thud of an object striking the ground beside you."
  9: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x001B [0x21] END_EVENT
 11: 0x001C [0x00] END_REQSTACK()
```
