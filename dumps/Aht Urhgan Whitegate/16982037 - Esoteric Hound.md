# 16982037 - Esoteric Hound

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 196 bytes                     |
| Total Events     | 7                             |
| References Count | 9                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [229](#event-229)        | 0x0001       |     28 |              8 |
| [221](#event-221)        | 0x001D       |      1 |              1 |
| [225](#event-225)        | 0x001E       |     28 |              8 |
| [65535.1](#event-655351) | 0x003A       |     31 |              7 |
| [65535.2](#event-655352) | 0x0059       |     24 |              6 |
| [3097](#event-3097)      | 0x0071       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003C      |          60 |
|       1 | 0x1243      |        4675 |
|       2 | 0x1244      |        4676 |
|       3 | 0x000D      |          13 |
|       4 | 0xFFFFFEA3  |  4294966947 |
|       5 | 0xFFFE6081  |  4294860929 |
|       6 | 0x0000      |           0 |
|       7 | 0xFFFFF66E  |  4294964846 |
|       8 | 0xFFFE668D  |  4294862477 |

## String References

- **4675**: Please buy a ticket at the counter if you wish to board the ship.
- **4676**: This is the entrance to the pier.

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

### Event 229

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 21 00           ...tlk0...#!.   
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=4675*)
    → "Please buy a ticket at the counter if you wish to board the ship."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x21] END_EVENT
  7: 0x001C [0x00] END_REQSTACK()
```

### Event 221

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         00                     .  
```

#### Opcodes

```
  0: 0x001D [0x00] END_REQSTACK()
```

### Event 225

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            1E F0                ..
0020: FF FF 7F 6F 70 66 00 80  F8 FF FF 7F F8 FF FF 7F  ...opf..........
0030: 74 6C 6B 30 1D 02 80 23  21 00                    tlk0...#!.      
```

#### Opcodes

```
  0: 0x001E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0023 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0024 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0025 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
  4: 0x0034 [0x1D] PRINT_EVENT_MESSAGE(message_id=4676*)
    → "This is the entrance to the pier."
  5: 0x0037 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0038 [0x21] END_EVENT
  7: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 31 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                32 03 80 1F 00 04            2.....
0040: 80 05 80 06 80 1F 01 1F  00 07 80 05 80 06 80 1F  ................
0050: 01 4B F8 FF FF 7F 06 80  00                       .K.......       
```

#### Opcodes

```
  0: 0x003A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003D [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.349*, Z=-106.367*, Y=0.000*
  2: 0x0045 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0047 [0x1F] MOVE_ENTITY: EventEntity moves to X=-2.450*, Z=-106.367*, Y=0.000*
  4: 0x004F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0051 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=0.0°*)
  6: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             32 03 80 1F 00 04 80           2......
0060: 05 80 06 80 1F 01 1F 00  04 80 08 80 06 80 1F 01  ................
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0059 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005C [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.349*, Z=-106.367*, Y=0.000*
  2: 0x0064 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0066 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.349*, Z=-104.819*, Y=0.000*
  4: 0x006E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0070 [0x00] END_REQSTACK()
```

### Event 3097

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0071  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    00                                              .              
```

#### Opcodes

```
  0: 0x0071 [0x00] END_REQSTACK()
```
