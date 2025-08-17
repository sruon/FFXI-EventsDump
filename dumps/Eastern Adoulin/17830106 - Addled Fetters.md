# 17830106 - Addled Fetters

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 168 bytes                 |
| Total Events     | 4                         |
| References Count | 11                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [529](#event-529)        | 0x0001       |     66 |             14 |
| [90](#event-90)          | 0x0043       |      1 |              1 |
| [65535.1](#event-655351) | 0x0044       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0041      |          65 |
|       1 | 0x290B      |       10507 |
|       2 | 0x003C      |          60 |
|       3 | 0x290C      |       10508 |
|       4 | 0x290D      |       10509 |
|       5 | 0x0028      |          40 |
|       6 | 0xFFFEC1B2  |  4294885810 |
|       7 | 0x282D      |       10285 |
|       8 | 0x0000      |           0 |
|       9 | 0xFFFEC049  |  4294885449 |
|      10 | 0x1031      |        4145 |

## String References

- **10507**: I saw someone slinking through the alleyways the other night. I could only describe him as a "shady gent."
- **10508**: Odd, I know. When I asked my superior about it, he told me people have spotted a guy fitting that description for years!
- **10509**: I h-h-hope it's not a ghost! I'm d-d-deathly afraid of ghosts! I can barely take a step without getting Galkabumps anymore.

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

### Event 529

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 66 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 62 30 1D  01 80 23 66 00 80 F8 FF  ...tlb0...#f....
0020: FF 7F F8 FF FF 7F 74 6C  62 31 66 02 80 F8 FF FF  ......tlb1f.....
0030: 7F F8 FF FF 7F 64 69 73  30 1D 03 80 23 1D 04 80  .....dis0...#...
0040: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=65*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=10507*)
    → "I saw someone slinking through the alleyways the other night. I could only describe him as a "shady gent.""
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=65*
  7: 0x002A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=60*
  8: 0x0039 [0x1D] PRINT_EVENT_MESSAGE(message_id=10508*)
    → "Odd, I know. When I asked my superior about it, he told me people have spotted a guy fitting that description for years!"
  9: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x003D [0x1D] PRINT_EVENT_MESSAGE(message_id=10509*)
    → "I h-h-hope it's not a ghost! I'm d-d-deathly afraid of ghosts! I can barely take a step without getting Galkabumps anymore."
 11: 0x0040 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0041 [0x21] END_EVENT
 13: 0x0042 [0x00] END_REQSTACK()
```

### Event 90

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0043  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          00                                          .            
```

#### Opcodes

```
  0: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             32 05 80 1F  00 06 80 07 80 08 80 1F      2...........
0050: 01 1F 00 09 80 0A 80 08  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x0044 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0047 [0x1F] MOVE_ENTITY: EventEntity moves to X=-81.486*, Z=10.285*, Y=0.000*
  2: 0x004F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0051 [0x1F] MOVE_ENTITY: EventEntity moves to X=-81.847*, Z=4.145*, Y=0.000*
  4: 0x0059 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x005B [0x00] END_REQSTACK()
```
