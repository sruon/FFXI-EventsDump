# 17793082 - Raging Tiger

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Selbina (ID: 248) |
| Block Size       | 144 bytes         |
| Total Events     | 6                 |
| References Count | 9                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [214](#event-214)        | 0x0001       |     28 |              8 |
| [221](#event-221)        | 0x001D       |      1 |              1 |
| [229](#event-229)        | 0x001E       |      1 |              1 |
| [65535.1](#event-655351) | 0x001F       |     19 |              5 |
| [65535.2](#event-655352) | 0x0032       |     17 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003C      |          60 |
|       1 | 0x1B85      |        7045 |
|       2 | 0x000D      |          13 |
|       3 | 0x8B87      |       35719 |
|       4 | 0xFFFF8E77  |  4294938231 |
|       5 | 0xFFFFF602  |  4294964738 |
|       6 | 0x83E2      |       33762 |
|       7 | 0xFFFF8F50  |  4294938448 |
|       8 | 0x03A0      |         928 |

## String References

- **7045**: Hey, I'm just a guard. Talk to Lucia, okay?

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

### Event 214

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
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7045*)
    → "Hey, I'm just a guard. Talk to Lucia, okay?"
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

### Event 229

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            00                   . 
```

#### Opcodes

```
  0: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               32                 2
0020: 02 80 1F 00 03 80 04 80  05 80 1F 01 1E F0 FF FF  ................
0030: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x001F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=35.719*, Z=-29.065*, Y=-2.558*
  2: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002C [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       32 02 80 1F 00 06  80 07 80 05 80 1F 01 39    2............9
0040: 08 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0032 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0035 [0x1F] MOVE_ENTITY: EventEntity moves to X=33.762*, Z=-28.848*, Y=-2.558*
  2: 0x003D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003F [0x39] SET_ENTITY_DIRECTION(direction=5.1°*)
  4: 0x0042 [0x00] END_REQSTACK()
```
