# 17788939 - Bald Aurochs

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Rabao (ID: 247) |
| Block Size       | 316 bytes       |
| Total Events     | 2               |
| References Count | 13              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [53](#event-53)       | 0x0001       |    238 |             39 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x273A      |       10042 |
|       1 | 0x273B      |       10043 |
|       2 | 0x0000      |           0 |
|       3 | 0x000A      |          10 |
|       4 | 0x0014      |          20 |
|       5 | 0x001E      |          30 |
|       6 | 0x0028      |          40 |
|       7 | 0x0032      |          50 |
|       8 | 0x003C      |          60 |
|       9 | 0x0005      |           5 |
|      10 | 0x0050      |          80 |
|      11 | 0x00EE      |         238 |
|      12 | 0x0236      |         566 |

## String References

- **10042**: A little further north of here is the Rabao oasis. It's not much, but there are goods for sale in the tents.
- **10043**: Outside of Rabao, the desert stretches for as far as the eye can see. Rabao is the only place to gather supplies for your journey and acts as a waypoint for adventurers. It's important for us to work together out here.

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

### Event 53

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 238 bytes |
| Instructions | 15        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1A 11 00 1A 8F 00 1D  00 80 23 1D 01 80 23 21   .........#...#!
0010: 00 86 00 F8 FF FF 7F 1E  F0 FF FF 7F 6F 70 1B 66  ............op.f
0020: 02 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 66  ..........tlk0.f
0030: 02 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 1B 66  ..........tlk1.f
0040: 03 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 66  ..........tlk0.f
0050: 04 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 66  ..........tlk0.f
0060: 05 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 66  ..........tlk0.f
0070: 06 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 66  ..........tlk0.f
0080: 07 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 66  ..........tlk0.f
0090: 08 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 5B  ..........tlk0.[
00A0: 09 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 5B  ..........tlk0.[
00B0: 0A 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 5B  ..........tlk0.[
00C0: 0B 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 5B  ..........tlk0.[
00D0: 0C 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 5B  ..........tlk0.[
00E0: 08 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 62 30 1B     ..........tlb0. 
```

#### Opcodes

```
  0: 0x0001 [0x1A] CALL_SUBROUTINE(address=0x0011)
  1: 0x0004 [0x1A] CALL_SUBROUTINE(address=0x008F)
  2: 0x0007 [0x1D] PRINT_EVENT_MESSAGE(message_id=10042*)
    → "A little further north of here is the Rabao oasis. It's not much, but there are goods for sale in the tents."
  3: 0x000A [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000B [0x1D] PRINT_EVENT_MESSAGE(message_id=10043*)
    → "Outside of Rabao, the desert stretches for as far as the eye can see. Rabao is the only place to gather supplies for your journey and acts as a waypoint for adventurers. It's important for us to work together out here."
  5: 0x000E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000F [0x21] END_EVENT
  7: 0x0010 [0x00] END_REQSTACK()

SUBROUTINE_0011:
  8: 0x0011 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  9: 0x0017 [0x1E] EventEntity looks at LocalPlayer and starts talking
 10: 0x001C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 11: 0x001D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 12: 0x001E [0x1B] RETURN

SUBROUTINE_008F:
 13: 0x008F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
 14: 0x009E [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=0*
     0x002E [0x1B] RETURN
     0x002F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=0*
     0x003E [0x1B] RETURN
     0x003F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=10*
     0x004E [0x1B] RETURN
     0x004F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
     0x005E [0x1B] RETURN
     0x005F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
     0x006E [0x1B] RETURN
     0x006F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
     0x007E [0x1B] RETURN
     0x007F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
     0x008E [0x1B] RETURN
# Dead code (unreachable instructions):
     0x009F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=5*
     0x00AE [0x1B] RETURN
     0x00AF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=80*
     0x00BE [0x1B] RETURN
     0x00BF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=238*
     0x00CE [0x1B] RETURN
     0x00CF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=566*
     0x00DE [0x1B] RETURN
     0x00DF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=60*
     0x00EE [0x1B] RETURN
```
