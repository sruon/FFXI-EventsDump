# 17809442 - Paito-Maito

## Common Data

| Field            | Value          |
|------------------|----------------|
| Zone             | Norg (ID: 252) |
| Block Size       | 328 bytes      |
| Total Events     | 2              |
| References Count | 13             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [90](#event-90)       | 0x0001       |    250 |             39 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x2870      |       10352 |
|       2 | 0x2871      |       10353 |
|       3 | 0x0000      |           0 |
|       4 | 0x000A      |          10 |
|       5 | 0x0014      |          20 |
|       6 | 0x001E      |          30 |
|       7 | 0x0032      |          50 |
|       8 | 0x003C      |          60 |
|       9 | 0x0005      |           5 |
|      10 | 0x0050      |          80 |
|      11 | 0x00EE      |         238 |
|      12 | 0x0236      |         566 |

## String References

- **10352**: I'm the gaudy-bodyguard of this place. You make one wrong move, and I will smack and kick and punch and whack and pummel and smash and crush and grind your bones into powder...and then kick you some more.
- **10353**: You follow the rules, I'll let you live. You break them, I break you.

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

### Event 90

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 250 bytes |
| Instructions | 13        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1A 1D 00 66 00 80 F8  FF FF 7F F8 FF FF 7F 77   ...f..........w
0010: 61 69 30 1D 01 80 23 1D  02 80 23 21 00 86 00 F8  ai0...#...#!....
0020: FF FF 7F 1E F0 FF FF 7F  6F 70 1B 66 03 80 F8 FF  ........op.f....
0030: FF 7F F8 FF FF 7F 74 6C  6B 30 1B 66 03 80 F8 FF  ......tlk0.f....
0040: FF 7F F8 FF FF 7F 74 6C  6B 31 1B 66 04 80 F8 FF  ......tlk1.f....
0050: FF 7F F8 FF FF 7F 74 6C  6B 30 1B 66 05 80 F8 FF  ......tlk0.f....
0060: FF 7F F8 FF FF 7F 74 6C  6B 30 1B 66 06 80 F8 FF  ......tlk0.f....
0070: FF 7F F8 FF FF 7F 74 6C  6B 30 1B 66 00 80 F8 FF  ......tlk0.f....
0080: FF 7F F8 FF FF 7F 74 6C  6B 30 1B 66 07 80 F8 FF  ......tlk0.f....
0090: FF 7F F8 FF FF 7F 74 6C  6B 30 1B 66 08 80 F8 FF  ......tlk0.f....
00A0: FF 7F F8 FF FF 7F 74 6C  6B 30 1B 5B 09 80 F8 FF  ......tlk0.[....
00B0: FF 7F F8 FF FF 7F 74 6C  6B 30 1B 5B 0A 80 F8 FF  ......tlk0.[....
00C0: FF 7F F8 FF FF 7F 74 6C  6B 30 1B 5B 0B 80 F8 FF  ......tlk0.[....
00D0: FF 7F F8 FF FF 7F 74 6C  6B 30 1B 5B 0C 80 F8 FF  ......tlk0.[....
00E0: FF 7F F8 FF FF 7F 74 6C  6B 30 1B 5B 08 80 F8 FF  ......tlk0.[....
00F0: FF 7F F8 FF FF 7F 74 6C  62 30 1B                 ......tlb0.     
```

#### Opcodes

```
  0: 0x0001 [0x1A] CALL_SUBROUTINE(address=0x001D)
  1: 0x0004 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "wai0" with entities [EventEntity, EventEntity], work=40*
  2: 0x0013 [0x1D] PRINT_EVENT_MESSAGE(message_id=10352*)
    → "I'm the gaudy-bodyguard of this place. You make one wrong move, and I will smack and kick and punch and whack and pummel and smash and crush and grind your bones into powder...and then kick you some more."
  3: 0x0016 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=10353*)
    → "You follow the rules, I'll let you live. You break them, I break you."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x21] END_EVENT
  7: 0x001C [0x00] END_REQSTACK()

SUBROUTINE_001D:
  8: 0x001D [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  9: 0x0023 [0x1E] EventEntity looks at LocalPlayer and starts talking
 10: 0x0028 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 11: 0x0029 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 12: 0x002A [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x002B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=0*
     0x003A [0x1B] RETURN
     0x003B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=0*
     0x004A [0x1B] RETURN
     0x004B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=10*
     0x005A [0x1B] RETURN
     0x005B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
     0x006A [0x1B] RETURN
     0x006B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
     0x007A [0x1B] RETURN
     0x007B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
     0x008A [0x1B] RETURN
     0x008B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
     0x009A [0x1B] RETURN
     0x009B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
     0x00AA [0x1B] RETURN
     0x00AB [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=5*
     0x00BA [0x1B] RETURN
     0x00BB [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=80*
     0x00CA [0x1B] RETURN
     0x00CB [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=238*
     0x00DA [0x1B] RETURN
     0x00DB [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=566*
     0x00EA [0x1B] RETURN
     0x00EB [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=60*
     0x00FA [0x1B] RETURN
```
