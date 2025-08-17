# 17134051 - Helmfried

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Bastok Markets [S] (ID: 87) |
| Block Size       | 88 bytes                    |
| Total Events     | 3                           |
| References Count | 4                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [151](#event-151)     | 0x0001       |     33 |              9 |
| [179](#event-179)     | 0x0022       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x003C      |          60 |
|       2 | 0x301B      |       12315 |
|       3 | 0x301C      |       12316 |

## String References

- **12315**: Before the onset of war, President Prien rallied the strong support of the Galkan citizenry. That was the key to his winning the election.
- **12316**: But it seems his campaign promises of improving living standards have been complicated by the outbreak of hostilities.

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

### Event 151

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 5B 01 80 F8 FF FF 7F   ........[......
0010: F8 FF FF 7F 74 6C 62 30  1D 02 80 23 1D 03 80 23  ....tlb0...#...#
0020: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=60*
  3: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=12315*)
    → "Before the onset of war, President Prien rallied the strong support of the Galkan citizenry. That was the key to his winning the election."
  4: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=12316*)
    → "But it seems his campaign promises of improving living standards have been complicated by the outbreak of hostilities."
  6: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0020 [0x21] END_EVENT
  8: 0x0021 [0x00] END_REQSTACK()
```

### Event 179

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0022  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       92 01 F8 FF FF 7F  00                         .......       
```

#### Opcodes

```
  0: 0x0022 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0028 [0x00] END_REQSTACK()
```
