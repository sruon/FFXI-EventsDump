# 17784902 - Pitantimand

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Port Jeuno (ID: 246) |
| Block Size       | 228 bytes            |
| Total Events     | 4                    |
| References Count | 7                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [62](#event-62)       | 0x0001       |     56 |             10 |
| [63](#event-63)       | 0x0039       |     56 |             10 |
| [64](#event-64)       | 0x0071       |     55 |             17 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x1BCA      |        7114 |
|       2 | 0x1BCB      |        7115 |
|       3 | 0x1BCC      |        7116 |
|       4 | 0x0000      |           0 |
|       5 | 0x1BCE      |        7118 |
|       6 | 0x1BCF      |        7119 |

## String References

- **7114**: Somebody just tried to smuggle in some contraband. You should watch out for scum like that.
- **7115**: What could those smugglers be thinking? I know the penalties are light, but it's such a careless thing to do.
- **7116**: If someone's in need, I'll gladly sign.
- **7118**: The petition is complete.
- **7119**: You have $0 more [signature/signatures] to go.

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

### Event 62

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 56 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 66 00 80 F8 FF  ...tlk0...#f....
0020: FF 7F F8 FF FF 7F 74 6C  6B 31 53 F8 FF FF 7F F8  ......tlk1S.....
0030: FF FF 7F 74 6C 6B 31 21  00                       ...tlk1!.       
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7114*)
    → "Somebody just tried to smuggle in some contraband. You should watch out for scum like that."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
  7: 0x002A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  8: 0x0037 [0x21] END_EVENT
  9: 0x0038 [0x00] END_REQSTACK()
```

### Event 63

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 56 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             1E F0 FF FF 7F 6F 70           .....op
0040: 66 00 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 1D  f..........tlk0.
0050: 02 80 23 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
0060: 6B 31 53 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 21  k1S........tlk1!
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0039 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x003F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0040 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=7115*)
    → "What could those smugglers be thinking? I know the penalties are light, but it's such a careless thing to do."
  5: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0053 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
  7: 0x0062 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  8: 0x006F [0x21] END_EVENT
  9: 0x0070 [0x00] END_REQSTACK()
```

### Event 64

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 55 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    20 01 42 1E F0 FF FF  7F 6F 70 66 00 80 F8 FF    .B.....opf....
0080: FF 7F F8 FF FF 7F 74 6C  6B 30 1D 03 80 23 5E 69  ......tlk0...#^i
0090: 64 6C 30 02 02 10 04 80  00 A2 00 48 05 80 23 01  dl0........H..#.
00A0: A6 00 48 06 80 23 21 00                           ..H..#!.        
```

#### Opcodes

```
  0: 0x0071 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0073 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0074 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0079 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x007A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x007B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  6: 0x008A [0x1D] PRINT_EVENT_MESSAGE(message_id=7116*)
    → "If someone's in need, I'll gladly sign."
  7: 0x008D [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x008E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  9: 0x0093 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x00A2
 10: 0x009B [0x48] [System] [7118*]:
    → "The petition is complete."
 11: 0x009E [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x009F [0x01] GOTO 0x00A6
 13: 0x00A2 [0x48] [System] [7119*]:
    → "You have $0 more [signature/signatures] to go."
 14: 0x00A5 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00A6:
 15: 0x00A6 [0x21] END_EVENT
 16: 0x00A7 [0x00] END_REQSTACK()
```
