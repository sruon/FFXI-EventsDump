# 17809436 - Louartain

## Common Data

| Field            | Value          |
|------------------|----------------|
| Zone             | Norg (ID: 252) |
| Block Size       | 348 bytes      |
| Total Events     | 5              |
| References Count | 14             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [84](#event-84)       | 0x0001       |     16 |              8 |
| [209](#event-209)     | 0x0011       |      1 |              1 |
| [210](#event-210)     | 0x0012       |      1 |              1 |
| [224](#event-224)     | 0x0013       |    234 |             37 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2851      |       10321 |
|       1 | 0x2852      |       10322 |
|       2 | 0x2B74      |       11124 |
|       3 | 0x0000      |           0 |
|       4 | 0x000A      |          10 |
|       5 | 0x0014      |          20 |
|       6 | 0x001E      |          30 |
|       7 | 0x0028      |          40 |
|       8 | 0x0032      |          50 |
|       9 | 0x003C      |          60 |
|      10 | 0x0005      |           5 |
|      11 | 0x0050      |          80 |
|      12 | 0x00EE      |         238 |
|      13 | 0x0236      |         566 |

## String References

- **10321**: When we pirates attack other ships, we call up the souls of those lost at sea to do our dirty work. It's a little bit different from the summoning magic you adventurers use.
- **10322**: But don't ask me to explain how. I ain't no magician, you know.
- **11124**: Those boys ain't gonna be satisfied, no matter what you bring. Yer better off just goin' on yer way.

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

### Event 84

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1A 1F 00 1A 5D 00 1D  00 80 23 1D 01 80 23 21   ....]....#...#!
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x1A] CALL_SUBROUTINE(address=0x001F)
  1: 0x0004 [0x1A] CALL_SUBROUTINE(address=0x005D)
  2: 0x0007 [0x1D] PRINT_EVENT_MESSAGE(message_id=10321*)
    → "When we pirates attack other ships, we call up the souls of those lost at sea to do our dirty work. It's a little bit different from the summoning magic you adventurers use."
  3: 0x000A [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000B [0x1D] PRINT_EVENT_MESSAGE(message_id=10322*)
    → "But don't ask me to explain how. I ain't no magician, you know."
  5: 0x000E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000F [0x21] END_EVENT
  7: 0x0010 [0x00] END_REQSTACK()
```

### Event 209

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    00                                              .              
```

#### Opcodes

```
  0: 0x0011 [0x00] END_REQSTACK()
```

### Event 210

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0012  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       00                                            .             
```

#### Opcodes

```
  0: 0x0012 [0x00] END_REQSTACK()
```

### Event 224

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0013    |
| Data Size    | 234 bytes |
| Instructions | 13        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          1A 1F 00 1A 5D  00 1D 02 80 23 21 00 86     ....]....#!..
0020: 00 F8 FF FF 7F 1E F0 FF  FF 7F 6F 70 1B 66 03 80  ..........op.f..
0030: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1B 66 03 80  ........tlk0.f..
0040: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 1B 66 04 80  ........tlk1.f..
0050: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1B 66 05 80  ........tlk0.f..
0060: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1B 66 06 80  ........tlk0.f..
0070: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1B 66 07 80  ........tlk0.f..
0080: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1B 66 08 80  ........tlk0.f..
0090: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1B 66 09 80  ........tlk0.f..
00A0: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1B 5B 0A 80  ........tlk0.[..
00B0: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1B 5B 0B 80  ........tlk0.[..
00C0: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1B 5B 0C 80  ........tlk0.[..
00D0: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1B 5B 0D 80  ........tlk0.[..
00E0: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1B 5B 09 80  ........tlk0.[..
00F0: F8 FF FF 7F F8 FF FF 7F  74 6C 62 30 1B           ........tlb0.   
```

#### Opcodes

```
  0: 0x0013 [0x1A] CALL_SUBROUTINE(address=0x001F)
  1: 0x0016 [0x1A] CALL_SUBROUTINE(address=0x005D)
  2: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=11124*)
    → "Those boys ain't gonna be satisfied, no matter what you bring. Yer better off just goin' on yer way."
  3: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x001D [0x21] END_EVENT
  5: 0x001E [0x00] END_REQSTACK()

SUBROUTINE_001F:
  6: 0x001F [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  7: 0x0025 [0x1E] EventEntity looks at LocalPlayer and starts talking
  8: 0x002A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x002B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 10: 0x002C [0x1B] RETURN

SUBROUTINE_005D:
 11: 0x005D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 12: 0x006C [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x002D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=0*
     0x003C [0x1B] RETURN
     0x003D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=0*
     0x004C [0x1B] RETURN
     0x004D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=10*
     0x005C [0x1B] RETURN
# Dead code (unreachable instructions):
     0x006D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
     0x007C [0x1B] RETURN
     0x007D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
     0x008C [0x1B] RETURN
     0x008D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
     0x009C [0x1B] RETURN
     0x009D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
     0x00AC [0x1B] RETURN
     0x00AD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=5*
     0x00BC [0x1B] RETURN
     0x00BD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=80*
     0x00CC [0x1B] RETURN
     0x00CD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=238*
     0x00DC [0x1B] RETURN
     0x00DD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=566*
     0x00EC [0x1B] RETURN
     0x00ED [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=60*
     0x00FC [0x1B] RETURN
```
