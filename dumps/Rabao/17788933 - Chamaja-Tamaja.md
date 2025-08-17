# 17788933 - Chamaja-Tamaja

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Rabao (ID: 247) |
| Block Size       | 348 bytes       |
| Total Events     | 6               |
| References Count | 12              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [45](#event-45)       | 0x0001       |    228 |             35 |
| [155](#event-155)     | 0x00E5       |      7 |              2 |
| [156](#event-156)     | 0x00EC       |      7 |              2 |
| [157](#event-157)     | 0x00F3       |      7 |              2 |
| [158](#event-158)     | 0x00FA       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2725      |       10021 |
|       1 | 0x0000      |           0 |
|       2 | 0x000A      |          10 |
|       3 | 0x0014      |          20 |
|       4 | 0x001E      |          30 |
|       5 | 0x0028      |          40 |
|       6 | 0x0032      |          50 |
|       7 | 0x003C      |          60 |
|       8 | 0x0005      |           5 |
|       9 | 0x0050      |          80 |
|      10 | 0x00EE      |         238 |
|      11 | 0x0236      |         566 |

## String References

- **10021**: After going through all the trouble of drawing up the water for the oasis, the pioneers of this place stocked it with fish. You can't argue with that kind of thoroughness, hehehe.

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

### Event 45

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 228 bytes |
| Instructions | 4         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 21 00 86  00 F8 FF FF 7F 1E F0 FF   ...#!..........
0010: FF 7F 6F 70 1B 66 01 80  F8 FF FF 7F F8 FF FF 7F  ..op.f..........
0020: 74 6C 6B 30 1B 66 01 80  F8 FF FF 7F F8 FF FF 7F  tlk0.f..........
0030: 74 6C 6B 31 1B 66 02 80  F8 FF FF 7F F8 FF FF 7F  tlk1.f..........
0040: 74 6C 6B 30 1B 66 03 80  F8 FF FF 7F F8 FF FF 7F  tlk0.f..........
0050: 74 6C 6B 30 1B 66 04 80  F8 FF FF 7F F8 FF FF 7F  tlk0.f..........
0060: 74 6C 6B 30 1B 66 05 80  F8 FF FF 7F F8 FF FF 7F  tlk0.f..........
0070: 74 6C 6B 30 1B 66 06 80  F8 FF FF 7F F8 FF FF 7F  tlk0.f..........
0080: 74 6C 6B 30 1B 66 07 80  F8 FF FF 7F F8 FF FF 7F  tlk0.f..........
0090: 74 6C 6B 30 1B 5B 08 80  F8 FF FF 7F F8 FF FF 7F  tlk0.[..........
00A0: 74 6C 6B 30 1B 5B 09 80  F8 FF FF 7F F8 FF FF 7F  tlk0.[..........
00B0: 74 6C 6B 30 1B 5B 0A 80  F8 FF FF 7F F8 FF FF 7F  tlk0.[..........
00C0: 74 6C 6B 30 1B 5B 0B 80  F8 FF FF 7F F8 FF FF 7F  tlk0.[..........
00D0: 74 6C 6B 30 1B 5B 07 80  F8 FF FF 7F F8 FF FF 7F  tlk0.[..........
00E0: 74 6C 62 30 1B                                    tlb0.           
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=10021*)
    → "After going through all the trouble of drawing up the water for the oasis, the pioneers of this place stocked it with fish. You can't argue with that kind of thoroughness, hehehe."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x21] END_EVENT
  3: 0x0006 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0007 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
     0x000D [0x1E] EventEntity looks at LocalPlayer and starts talking
     0x0012 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
     0x0013 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
     0x0014 [0x1B] RETURN
     0x0015 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=0*
     0x0024 [0x1B] RETURN
     0x0025 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=0*
     0x0034 [0x1B] RETURN
     0x0035 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=10*
     0x0044 [0x1B] RETURN
     0x0045 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
     0x0054 [0x1B] RETURN
     0x0055 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
     0x0064 [0x1B] RETURN
     0x0065 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
     0x0074 [0x1B] RETURN
     0x0075 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
     0x0084 [0x1B] RETURN
     0x0085 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
     0x0094 [0x1B] RETURN
     0x0095 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=5*
     0x00A4 [0x1B] RETURN
     0x00A5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=80*
     0x00B4 [0x1B] RETURN
     0x00B5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=238*
     0x00C4 [0x1B] RETURN
     0x00C5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=566*
     0x00D4 [0x1B] RETURN
     0x00D5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=60*
     0x00E4 [0x1B] RETURN
```

### Event 155

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00E5  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                92 01 F8  FF FF 7F 00                   .......    
```

#### Opcodes

```
  0: 0x00E5 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00EB [0x00] END_REQSTACK()
```

### Event 156

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00EC  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                      92 01 F8 FF              ....
00F0: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x00EC [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00F2 [0x00] END_REQSTACK()
```

### Event 157

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F3  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:          92 01 F8 FF FF  7F 00                       .......      
```

#### Opcodes

```
  0: 0x00F3 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00F9 [0x00] END_REQSTACK()
```

### Event 158

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00FA  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                92 01 F8 FF FF 7F            ......
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x00FA [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0100 [0x00] END_REQSTACK()
```
