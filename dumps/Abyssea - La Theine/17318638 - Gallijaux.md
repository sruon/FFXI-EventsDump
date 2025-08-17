# 17318638 - Gallijaux

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Abyssea - La Theine (ID: 132) |
| Block Size       | 188 bytes                     |
| Total Events     | 4                             |
| References Count | 11                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [174](#event-174)     | 0x0001       |     58 |             17 |
| [175](#event-175)     | 0x003B       |     25 |              9 |
| [176](#event-176)     | 0x0054       |     25 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x43EF      |       17391 |
|       1 | 0x1F16      |        7958 |
|       2 | 0x1F17      |        7959 |
|       3 | 0x000B      |          11 |
|       4 | 0x1F18      |        7960 |
|       5 | 0x00C9      |         201 |
|       6 | 0x0000      |           0 |
|       7 | 0x0019      |          25 |
|       8 | 0x1F15      |        7957 |
|       9 | 0x0024      |          36 |
|      10 | 0x1F19      |        7961 |

## String References

- **7957**: Why is it taking so long to mend a simple fishing rod? The poor folk here are soon like to die of starvation...
- **7958**: Why, this is the $0 I had sent to be repaired!
- **7959**: I had been expecting the craftsman's familiar face, but doubtless he's swamped with repair work.
- **7960**: Pray send my regards to my little brother when next you see him.
- **7961**: Now that the tool of my trade is returned to me, I had best return to my duty. 'Tis a weighty responsibility, ensuring that all mouths are fed.

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

### Event 174

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 58 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 1E F0 FF FF  7F 6F 70 03 02 10 00 80    .B.....op.....
0010: 1D 01 80 23 1D 02 80 23  6E EE 42 08 01 03 80 99  ...#...#n.B.....
0020: EE 42 08 01 1D 04 80 23  45 05 80 F0 FF FF 7F F0  .B.....#E.......
0030: FF FF 7F 71 73 74 63 06  80 21 00                 ...qstc..!.     
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0009 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x000A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x000B [0x03] Work_Zone[2] = 17391*
  6: 0x0010 [0x1D] PRINT_EVENT_MESSAGE(message_id=7958*)
    → "Why, this is the $0 I had sent to be repaired!"
  7: 0x0013 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0014 [0x1D] PRINT_EVENT_MESSAGE(message_id=7959*)
    → "I had been expecting the craftsman's familiar face, but doubtless he's swamped with repair work."
  9: 0x0017 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0018 [0x6E] Gallijaux (ID: 17318638/0x010842EE) uses emote 11*
 11: 0x001F [0x99] Wait for Gallijaux (ID: 17318638/0x010842EE) animation to complete
 12: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=7960*)
    → "Pray send my regards to my little brother when next you see him."
 13: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0028 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 15: 0x0039 [0x21] END_EVENT
 16: 0x003A [0x00] END_REQSTACK()
```

### Event 175

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 25 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   1E F0 FF FF 7F             .....
0040: 6F 70 6E EE 42 08 01 07  80 99 EE 42 08 01 1D 08  opn.B......B....
0050: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x003B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0040 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0041 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0042 [0x6E] Gallijaux (ID: 17318638/0x010842EE) uses emote 25*
  4: 0x0049 [0x99] Wait for Gallijaux (ID: 17318638/0x010842EE) animation to complete
  5: 0x004E [0x1D] PRINT_EVENT_MESSAGE(message_id=7957*)
    → "Why is it taking so long to mend a simple fishing rod? The poor folk here are soon like to die of starvation..."
  6: 0x0051 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0052 [0x21] END_EVENT
  8: 0x0053 [0x00] END_REQSTACK()
```

### Event 176

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 25 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             1E F0 FF FF  7F 6F 70 6E EE 42 08 01      .....opn.B..
0060: 09 80 99 EE 42 08 01 1D  0A 80 23 21 00           ....B.....#!.   
```

#### Opcodes

```
  0: 0x0054 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0059 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x005A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x005B [0x6E] Gallijaux (ID: 17318638/0x010842EE) uses emote 36*
  4: 0x0062 [0x99] Wait for Gallijaux (ID: 17318638/0x010842EE) animation to complete
  5: 0x0067 [0x1D] PRINT_EVENT_MESSAGE(message_id=7961*)
    → "Now that the tool of my trade is returned to me, I had best return to my duty. 'Tis a weighty responsibility, ensuring that all mouths are fed."
  6: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x006B [0x21] END_EVENT
  8: 0x006C [0x00] END_REQSTACK()
```
