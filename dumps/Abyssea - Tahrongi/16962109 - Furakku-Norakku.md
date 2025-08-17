# 16962109 - Furakku-Norakku

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Tahrongi (ID: 45) |
| Block Size       | 96 bytes                    |
| Total Events     | 2                           |
| References Count | 4                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [414](#event-414)     | 0x0001       |     53 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0029      |          41 |
|       1 | 0x1FD5      |        8149 |
|       2 | 0x0000      |           0 |
|       3 | 0x1FD6      |        8150 |

## String References

- **8149**: ...Huaaah...? There are scary monsters outside, but Ms. Fuepepe and that scowling Sibyl Guard are even scarier. I'll be safe here.
- **8150**: Refilling marshmallows? Would I have to go outside? I think I'll take a pass.

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

### Event 414

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 53 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 6E 6D 69 30 1D  01 80 23 02 02 10 02 80  ...nmi0...#.....
0020: 01 34 00 53 F8 FF FF 7F  F8 FF FF 7F 6E 6D 69 30  .4.S........nmi0
0030: 1D 03 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "nmi0" with entities [EventEntity, EventEntity], work=41*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=8149*)
    → "...Huaaah...? There are scary monsters outside, but Ms. Fuepepe and that scowling Sibyl Guard are even scarier. I'll be safe here."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0034
  7: 0x0023 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "nmi0" with entities [EventEntity, EventEntity]
  8: 0x0030 [0x1D] PRINT_EVENT_MESSAGE(message_id=8150*)
    → "Refilling marshmallows? Would I have to go outside? I think I'll take a pass."
  9: 0x0033 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0034 [0x21] END_EVENT
 11: 0x0035 [0x00] END_REQSTACK()
```
