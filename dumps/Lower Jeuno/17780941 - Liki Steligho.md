# 17780941 - Liki Steligho

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 208 bytes             |
| Total Events     | 4                     |
| References Count | 11                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [10097](#event-10097) | 0x0001       |     55 |             17 |
| [10098](#event-10098) | 0x0038       |     72 |             20 |
| [10125](#event-10125) | 0x0080       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x26BA      |        9914 |
|       1 | 0x0016      |          22 |
|       2 | 0x26BB      |        9915 |
|       3 | 0x0010      |          16 |
|       4 | 0x26BC      |        9916 |
|       5 | 0x0015      |          21 |
|       6 | 0x26BD      |        9917 |
|       7 | 0x001D      |          29 |
|       8 | 0x26BE      |        9918 |
|       9 | 0x0019      |          25 |
|      10 | 0x26BF      |        9919 |

## String References

- **9914**: Let me guess. That trrreasure chest over there has caught your eye, hasn't it? That's something the boss brought back from her latest scouting excurrrsion.
- **9915**: But would you believe it? We've trrried all of our keys and lockpicks, but to no avail. It just sits there sealed tight, mocking us all!
- **9916**: In fact, I'm so sick of looking at the darrrn thing that I'll make you a deal. Figure out how to open it, and you can help yourself to the contents, no questions asked!
- **9917**: Wh-wh-wh-what? Are my eyes to be trrrusted? How in the name of the Goddess did you manage to open that thing?
- **9918**: No, no...you'd better not tell me.
- **9919**: This is one rrriddle that I need to figure out for myself. That's Mithra pride, you know? You just run along with your trrreasure now.

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

### Event 10097

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 55 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 1E F0 FF  FF 7F 6F 70 6E CD 50 0F   ...#.....opn.P.
0010: 01 01 80 99 CD 50 0F 01  1D 02 80 23 99 CD 50 0F  .....P.....#..P.
0020: 01 6E CD 50 0F 01 03 80  99 CD 50 0F 01 1D 04 80  .n.P......P.....
0030: 23 99 CD 50 0F 01 21 00                           #..P..!.        
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=9914*)
    → "Let me guess. That trrreasure chest over there has caught your eye, hasn't it? That's something the boss brought back from her latest scouting excurrrsion."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x000A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x000B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x000C [0x6E] Liki Steligho (ID: 17780941/0x010F50CD) uses emote 22*
  6: 0x0013 [0x99] Wait for Liki Steligho (ID: 17780941/0x010F50CD) animation to complete
  7: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=9915*)
    → "But would you believe it? We've trrried all of our keys and lockpicks, but to no avail. It just sits there sealed tight, mocking us all!"
  8: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x001C [0x99] Wait for Liki Steligho (ID: 17780941/0x010F50CD) animation to complete
 10: 0x0021 [0x6E] Liki Steligho (ID: 17780941/0x010F50CD) uses emote 16*
 11: 0x0028 [0x99] Wait for Liki Steligho (ID: 17780941/0x010F50CD) animation to complete
 12: 0x002D [0x1D] PRINT_EVENT_MESSAGE(message_id=9916*)
    → "In fact, I'm so sick of looking at the darrrn thing that I'll make you a deal. Figure out how to open it, and you can help yourself to the contents, no questions asked!"
 13: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0031 [0x99] Wait for Liki Steligho (ID: 17780941/0x010F50CD) animation to complete
 15: 0x0036 [0x21] END_EVENT
 16: 0x0037 [0x00] END_REQSTACK()
```

### Event 10098

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 72 bytes |
| Instructions | 20       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          1E F0 FF FF 7F 6F 70 6E          .....opn
0040: CD 50 0F 01 05 80 99 CD  50 0F 01 1D 06 80 23 99  .P......P.....#.
0050: CD 50 0F 01 6E CD 50 0F  01 07 80 99 CD 50 0F 01  .P..n.P......P..
0060: 1D 08 80 23 99 CD 50 0F  01 6E CD 50 0F 01 09 80  ...#..P..n.P....
0070: 99 CD 50 0F 01 1D 0A 80  23 99 CD 50 0F 01 21 00  ..P.....#..P..!.
```

#### Opcodes

```
  0: 0x0038 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x003E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x003F [0x6E] Liki Steligho (ID: 17780941/0x010F50CD) uses emote 21*
  4: 0x0046 [0x99] Wait for Liki Steligho (ID: 17780941/0x010F50CD) animation to complete
  5: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=9917*)
    → "Wh-wh-wh-what? Are my eyes to be trrrusted? How in the name of the Goddess did you manage to open that thing?"
  6: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x004F [0x99] Wait for Liki Steligho (ID: 17780941/0x010F50CD) animation to complete
  8: 0x0054 [0x6E] Liki Steligho (ID: 17780941/0x010F50CD) uses emote 29*
  9: 0x005B [0x99] Wait for Liki Steligho (ID: 17780941/0x010F50CD) animation to complete
 10: 0x0060 [0x1D] PRINT_EVENT_MESSAGE(message_id=9918*)
    → "No, no...you'd better not tell me."
 11: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0064 [0x99] Wait for Liki Steligho (ID: 17780941/0x010F50CD) animation to complete
 13: 0x0069 [0x6E] Liki Steligho (ID: 17780941/0x010F50CD) uses emote 25*
 14: 0x0070 [0x99] Wait for Liki Steligho (ID: 17780941/0x010F50CD) animation to complete
 15: 0x0075 [0x1D] PRINT_EVENT_MESSAGE(message_id=9919*)
    → "This is one rrriddle that I need to figure out for myself. That's Mithra pride, you know? You just run along with your trrreasure now."
 16: 0x0078 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0079 [0x99] Wait for Liki Steligho (ID: 17780941/0x010F50CD) animation to complete
 18: 0x007E [0x21] END_EVENT
 19: 0x007F [0x00] END_REQSTACK()
```

### Event 10125

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0080  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0080 [0x00] END_REQSTACK()
```
