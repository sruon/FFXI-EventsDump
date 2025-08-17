# 16883824 - Angieurol

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 200 bytes                   |
| Total Events     | 3                           |
| References Count | 5                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [361](#event-361)     | 0x0001       |     74 |             10 |
| [362](#event-362)     | 0x004B       |     74 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x004B      |          75 |
|       1 | 0x2B4F      |       11087 |
|       2 | 0x2B50      |       11088 |
|       3 | 0x2B51      |       11089 |
|       4 | 0x2B52      |       11090 |

## String References

- **11087**: All the adults say it's too dangerous to go outside and play on the coast, but I'm sick of spending all day locked up in this cave.
- **11089**: Lo\`ok what Ma\`kki ga\`ve me!t

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

### Event 361

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 74 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0010: 1D 01 80 23 5B 00 80 F8  FF FF 7F F8 FF FF 7F 74  ...#[..........t
0020: 6C 6B 31 5B 00 80 71 A0  01 01 71 A0 01 01 74 6C  lk1[..q...q...tl
0030: 6B 30 2B 71 A0 01 01 02  80 23 5B 00 80 71 A0 01  k0+q.....#[..q..
0040: 01 71 A0 01 01 74 6C 6B  31 21 00                 .q...tlk1!.     
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=75*
  1: 0x0010 [0x1D] PRINT_EVENT_MESSAGE(message_id=11087*)
    → "All the adults say it's too dangerous to go outside and play on the coast, but I'm sick of spending all day locked up in this cave."
  2: 0x0013 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0014 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=75*
  4: 0x0023 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Evindigar (ID: 16883825/0x0101A071), Evindigar (ID: 16883825/0x0101A071)], work=75*
  5: 0x0032 [0x2B] Evindigar (ID: 16883825/0x0101A071) [11088*]:
    → "Yeah, I wish we could go out adventuring like the Chebukkis!"
  6: 0x0039 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x003A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Evindigar (ID: 16883825/0x0101A071), Evindigar (ID: 16883825/0x0101A071)], work=75*
  8: 0x0049 [0x21] END_EVENT
  9: 0x004A [0x00] END_REQSTACK()
```

### Event 362

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 74 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   5B 00 80 F8 FF             [....
0050: FF 7F F8 FF FF 7F 74 6C  6B 30 1D 03 80 23 5B 00  ......tlk0...#[.
0060: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 31 5B 00 80  .........tlk1[..
0070: 71 A0 01 01 71 A0 01 01  74 6C 6B 30 2B 71 A0 01  q...q...tlk0+q..
0080: 01 04 80 23 5B 00 80 71  A0 01 01 71 A0 01 01 74  ...#[..q...q...t
0090: 6C 6B 31 21 00                                    lk1!.           
```

#### Opcodes

```
  0: 0x004B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=75*
  1: 0x005A [0x1D] PRINT_EVENT_MESSAGE(message_id=11089*)
    → "Lo`ok what Ma`kki ga`ve me!t"
  2: 0x005D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x005E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=75*
  4: 0x006D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Evindigar (ID: 16883825/0x0101A071), Evindigar (ID: 16883825/0x0101A071)], work=75*
  5: 0x007C [0x2B] Evindigar (ID: 16883825/0x0101A071) [11090*]:
    → "Hey! Kukki said that he was going to give that to me! I'm telling my mommy!"
  6: 0x0083 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0084 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Evindigar (ID: 16883825/0x0101A071), Evindigar (ID: 16883825/0x0101A071)], work=75*
  8: 0x0093 [0x21] END_EVENT
  9: 0x0094 [0x00] END_REQSTACK()
```
